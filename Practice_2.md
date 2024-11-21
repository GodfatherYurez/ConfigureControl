# Практическая работа №2

Студент: Абрамович Юрий Александрович.

Группа: ИКБО-22-23



## Задание 1

Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

```powershell
pip show matplotlib
```

![image](https://github.com/user-attachments/assets/a46e7c2a-97b1-4b1d-921b-7a6ba62c0f19)


Для установки пакеты напрямую можно скачать архив с пакетом или склонировать его с помощью git, а затем установить с помощью setup.py

## Задание 2

Вывести служебную информацию о пакете express (Java Script). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

```powershell
npm show express
```

![image](https://github.com/user-attachments/assets/bc8ba493-bd9b-4b6f-acd4-2814c35352a2)

Для установки пакета напрямую надо также скачать либо склонировать пакет, затем использовать npm install.

## Задание 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

Требуется установить graphviz на ПК, затем визуализировать .dot файлы с помощью утилиты.

```bash
digraph ExpressDependencies {
    node [shape=ellipse];
    "express" -> {"accepts", "depd", "fresh", "proxy-addr", "statuses", "body-parser", "encodeurl", "http-errors", "qs", "type-is", "content-type", "escape-html", "methods", "range-parser", "utils-merge",
"cookie", "etag", "on-finished", "safe-buffer", "vary", "debug", "finalhandler", "parseurl", "send"};
}
```

```bash
digraph MatplotlibDependencies {
    node [shape=ellipse];
    "matplotlib" -> {"contourpy", "cycler", "fonttools", "importlib-resources", "kiwisolver", "numpy", "packaging", "pillow", "pyparsing", "python-dateutil"};
}
```

![image](https://github.com/user-attachments/assets/7819244f-b3ee-4fe0-a0bb-414aa17f4732)


![image](https://github.com/user-attachments/assets/45f7440e-3b6f-40d2-a0b4-e4f0f5f606da)


## Задание 4

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

```c++
include "globals.mzn";

int: n = 6;
array[1..n] of var 0..9: nums;

constraint all_different(nums);

constraint sum(nums[1..3]) = sum(nums[4..6]);

constraint sum(nums[1..3]) >= 0;

solve satisfy;

output ["Ticket: \(nums)\n"];
```

![Скриншот 4. Результат работы](/images/prac2/Задание 4.png)

## Задание 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![image](https://github.com/user-attachments/assets/d1ce8533-08ed-429f-a963-73860728a51e)


## Задание 6

Hешить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

```c++
set of int: foo_versions = 1..2;
set of int: left_versions = 1..1;
set of int: right_versions = 1..1;
set of int: shared_versions = 1..2;
set of int: target_versions = 1..2;
set of int: root_versions = 1..1; 

var foo_versions: selected_foo;
var left_versions: selected_left;
var right_versions: selected_right;
var shared_versions: selected_shared;
var target_versions: selected_target;
var root_versions: selected_root;

constraint selected_root = 1;
constraint selected_foo = 1;
constraint selected_target = 2;
constraint selected_left = 1;
constraint selected_right = 1;
constraint selected_shared >= 1;
constraint selected_shared < 2;

solve satisfy;

output 
[
  "foo: ", show(selected_foo),".0.0", "\n",
  "left: ", show(selected_left),".0.0", "\n",
  "right: ", show(selected_right),".0.0", "\n",
  "shared: ", show(selected_shared),".0.0", "\n",
  "target: ", show(selected_target),".0.0", "\n",
  "root: ", show(selected_root),".0.0", "\n"
];
```

![image](https://github.com/user-attachments/assets/65d13fb6-e83a-460e-80ea-0f69cd415801)

