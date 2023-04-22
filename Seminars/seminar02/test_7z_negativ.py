from checkout import checkout

pass_dir = "/home/user/tst"
path_arx = "/home/user/arx3.7z"
path_to_dir = "/home/user"


def test_step4():
    # test4
    assert checkout("cd {}; 7z e {} -o{} -y".format(pass_dir, path_arx, path_to_dir), "Is not archive"), "test4 Fail"


def test_step5():
    # test5
    assert checkout("cd /home/user; 7z t arx3.7z", "Is not archive"), "test5 Fail"
