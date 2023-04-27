from checkout import checkout_positive

folder_in = "/home/user/tst/file"
folder_out = "/home/user/tst/out"
folder_ext = "/home/user/tst/ext"
folder_ext2 = "/home/user/tst/ext2"
folder_tst = "/home/user/tst"


def test_step1(make_folders, clear_folders, make_files):
    # test1
    res1 = checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(folder_out), "arx.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_ext), item))
    assert all(res)


def test_step3():
    # test3
    assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert checkout_positive("cd {}; 7z u {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.7z".format(folder_out), item))
    assert all(res)


def test_step6(clear_folders, make_files, make_folders, make_subfolder):
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z x arx1.7z -o{} -y".format(folder_out, folder_ext2), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_ext2), item))
        res.append(checkout_positive("ls {}".format(folder_ext2), make_subfolder[0]))
        res.append(checkout_positive("ls {}/{}".format(folder_ext2, make_subfolder[0]), make_subfolder[1]))
    assert all(res)


def test_step7():
    assert checkout_positive("7z d {}/arx1.7z".format(folder_out), "Everything is Ok"), "Test7 Fail"


# def test_step8(make_files):
#     assert checkout_positive("cd {}; 7z a -t zip {}".format(folder_in, folder_out),
#                              "Everything is Ok"), "Test8 Fail"
