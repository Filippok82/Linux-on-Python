from checkout import checkout_negative

folder_out = "/home/user/tst"
folder_ext = "/home/user/tst/ext"
path_arx = "/home/user/tst/badarx.7z"


def test_step1(make_bad_arx):
    # test1
    assert checkout_negative("d {}; 7z e {} -o{} -y".format(folder_out, path_arx, folder_ext), "ERROR"), "Test4 Fail"


def test_step2(make_bad_arx):
    # test2
    assert checkout_negative("cd {}; 7z t {}".format(folder_out, path_arx), "ERROR"), "Test5 Fail"
