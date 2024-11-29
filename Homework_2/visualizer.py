import subprocess
import sys
import re

def get_dependencies(package, depth, current_depth=0):
    if current_depth >= depth:
        return []

    try:
        result = subprocess.run(['pacman', '-Qi', package], capture_output=True, text=True, check=True)
        package_info = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting info for {package}: {e}", file=sys.stderr)
        return []

    dependencies = []
    matches = re.findall(r"Depends On\s*:\s*(.*)", package_info)
    if matches:
        for dep_line in matches:
            for dep in dep_line.split():
                if dep != '>':
                    dep = dep.split('<')[0].split('=')[0].split('>')[0].split('!')[0]
                    dependencies.append(dep)

    transitive_deps = []
    for dep in dependencies:
        transitive_deps.extend(get_dependencies(dep, depth, current_depth + 1))

    return dependencies + transitive_deps

def generate_dot(package, dependencies):
    dot = f"digraph {package} {{\n"
    dot += f'  "{package}" [shape=box];\n'  # Mark the main package
    for dep in dependencies:
        dot += f'  "{package}" -> "{dep}";\n'
    dot += "}\n"
    return dot

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <graphviz_path> <package_name> <depth>", file=sys.stderr)
        sys.exit(1)

    graphviz_path = sys.argv[1]
    package = sys.argv[2]
    depth = int(sys.argv[3])

    dependencies = get_dependencies(package, depth)
    dependencies = list(set(dependencies))

    dot = generate_dot(package, dependencies)

    try:
        process = subprocess.Popen([graphviz_path, "-Tpng"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, error = process.communicate(dot.encode('utf-8'))
        if error:
            print(f"Graphviz error: {error.decode('utf-8')}", file=sys.stderr)
            sys.exit(1)

        sys.stdout.buffer.write(output)

    except FileNotFoundError:
        print(f"Error: Graphviz executable not found at {graphviz_path}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
