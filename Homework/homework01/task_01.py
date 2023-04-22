"""Условие:
Написать функцию на Python, которой передаются в качестве
параметров команда и текст. Функция должна возвращать True,
если команда успешно выполнена и текст найден в её выводе и
False в противном случае. Передаваться должна только одна строка,
разбиение вывода использовать не нужно."""

import subprocess


def func(*args):
    result = subprocess.run(args, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    print(out)
    if result.returncode == 0 and text in out:
        return True
    else:
        return False


if __name__ == '__main__':
    comand = "cat /home/user/test2.sh"
    text = 'echo "Homework01"'

    print(func(comand, text))
