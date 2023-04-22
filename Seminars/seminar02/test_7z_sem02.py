import subprocess

pass_dir = "/home/user/tst"
path_arx = "/home/user/arx1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    assert checkout("cd {}; 7z a {}".format(pass_dir, path_arx), "Everything is Ok"), "test1 Fail"


def test_step2():
    # test2
    assert checkout("cd {}; 7z u {}".format(pass_dir, path_arx), "Everything is Ok"), "test2 Fail"


def test_step3():
    # test3
    assert checkout("cd {}; 7z d {}".format(pass_dir, path_arx), "Everything is Ok"), "test3 Fail"
