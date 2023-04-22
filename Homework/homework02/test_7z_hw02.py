"""Задание№1
Условие:
Дополнитьь проект тестами, проверяющими команды ввода списка файлов(l)
и разархивирования с путями (x)
Задание№2
Установить пакет для расчета crc32
Доработать проект, добавив текст команды для расчета хеша
"""

from checkout02 import checkout02

pass_dir = "/home/user/tst"
path_arx = "/home/user/arx1"
path_file = "/home/user"
file = "arx1.7z"


def test_step1():
    # test1
    assert checkout02("cd {}; 7z a {}".format(pass_dir, path_arx), "Everything is Ok"), "test1 Fail"


def test_step2():
    # test2
    assert checkout02("cd {}; 7z u {}".format(pass_dir, path_arx), "Everything is Ok"), "test2 Fail"


def test_step3():
    # test3
    assert checkout02("cd {}; 7z d {}".format(pass_dir, path_arx), "Everything is Ok"), "test3 Fail"


def test_step6():
    # test6
    assert checkout02("cd {};7z l {}".format(path_file, file), "Listing archive: arx1.7z"), "test6 Fail"


def test_step7():
    # test7
    assert checkout02("cd {};7z x {}".format(path_file, file), "Everything is Ok"), "test7 Fail"


def test_step8():
    # test8
    assert checkout02("cd {};7z h {}".format(path_file, file), "Size: 32"), "test8 Fail"
