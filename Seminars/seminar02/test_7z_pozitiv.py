from checkout import checkout

pass_dir = "/home/user/tst"
path_arx = "/home/user/arx1"


def test_step1():
    # test1
    assert checkout("cd {}; 7z a {}".format(pass_dir, path_arx), "Everything is Ok"), "test1 Fail"


def test_step2():
    # test2
    assert checkout("cd {}; 7z u {}".format(pass_dir, path_arx), "Everything is Ok"), "test2 Fail"


def test_step3():
    # test3
    assert checkout("cd {}; 7z d {}".format(pass_dir, path_arx), "Everything is Ok"), "test3 Fail"


def test_step6():
    # test6
    assert checkout("cd /home/user; 7z l arx1.7z", "Listing archive: arx1.7z"), "test6 Fail"


def test_step7():
    # test7
    assert checkout("cd /home/user; 7z x arx1.7z", "Everything is Ok"), "test7 Fail"
