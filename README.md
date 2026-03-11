### Hexlet tests and linter status:

[![Actions Status](https://github.com/GrayFox-source/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/GrayFox-source/python-project-50/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=GrayFox-source_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=GrayFox-source_python-project-50)
[![Tests](https://github.com/GrayFox-source/python-project-50/actions/workflows/tests.yml/badge.svg)](https://github.com/GrayFox-source/python-project-50/actions/workflows/tests.yml)

## Описание:
<h3>Проект вычислитель отличий - это CLI утилита, позволяющая сравнивать 2 файла и выделять отличия, произошедшие в них.</h3>
<h4>На данный момент для сравнения доступны 2 типа файлов - json и yaml.</h4>

## Использование:

Для выявления справки об утилите:
```sh
gendiff -h
```
Пример вызова с выводом по умолчанию (stylish)

```sh
gendiff file1.json file2.json
```

## Опции утилиты

- `-h, --help` — отображение окна помощи и выход.
- `-f FORMAT, --format FORMAT` — задать формат вывода данных (поддерживаемые форматы: `plain`, `json`, `stylish`)


### Тесты

Чтобы запустить тесты, используйте заданную команду:

```sh
uv run pytest
or 
make test
```

Для проверки кода линтером, используйте:
```sh
make lint
```

## Примеры работы утилиты


[`Пример работы JSON файла`](https://asciinema.org/a/tmUn6jf8z2600qoA)
[`Пример работы Yaml файла`](https://asciinema.org/a/9oRHwB3EmApPURx0)
[`Пример вывода в plain и stylish форматах`](https://asciinema.org/a/U5R2Kt3n7Pcke4Af)
[`Пример вывода в json формате`](https://asciinema.org/a/hHFZlsPLK8OhWbKD)
