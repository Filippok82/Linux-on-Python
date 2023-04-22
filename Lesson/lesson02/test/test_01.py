import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    assert checkout('cd /home/user/tst; 7z a ../out/arx2', 'Everything is OK'), 'test1 FAIL'


def test_step2():
    assert checkout("cd /home/user/out, 7z e arx2.7z /home/zerg/folder1", 'Everything is OK'), 'test2 FAIL'

def test_step3():
    assert checkout('cd /home/user/out; 7z t arx2.7z', 'Everything is OK'), 'test3 FAIL'
