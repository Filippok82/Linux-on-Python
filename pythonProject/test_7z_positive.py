from checkout import checkout_positive, ssh_checkout
from load_file import upload_files
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step0(save_log, start_time):
    res = []
    upload_files(data["host"], data["user"], data["password"], data["local_path"], data["remote_path"])
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            f"echo {data['password']} | sudo -S dpkg -i {data['remote_path']}", "Настраивается пакет"))
    res.append(ssh_checkout(data["host"], data["user"], data["password"], f"echo {data['password']} "
                                                                          f"| sudo -S dpkg -s {data['pkgname']}",
                            "Status: install ok installed"))
    assert all(res), "Test Fail"


def test_step1(make_folders, clear_folders, make_files):
    # test1
    upload_files(data["host"], data["user"], data["password"], data["local_path"], data["remote_path"])
    res1 = ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {};" "7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"
    res2 = ssh_checkout(data["host"], data["user"], data["password"], "ls {}".format(data["folder_out"]),
                        "arx1.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                            "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            "cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                            "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], data["password"], "ls {}".format(data["folder_ext"]), item))
    assert all(res)


def test_step3():
    # test3
    assert ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(
            ssh_checkout(data["host"], data["user"], data["password"], "cd {}; 7z l arx1.7z".format(data["folder_out"]),
                         item))
    assert all(res)


def test_step6(clear_folders, make_files, make_folders, make_subfolder):
    res = []
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], data["password"],
                            "cd {}; 7z x arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext2"]),
                            "Everything is Ok"))
    for item in make_files:
        res.append(
            ssh_checkout(data["host"], data["user"], data["password"], "ls {}".format(data["folder_ext2"]), item))
        res.append(ssh_checkout(data["host"], data["user"], data["password"], "ls {}".format(data["folder_ext2"]),
                                make_subfolder[0]))
        res.append(ssh_checkout(data["host"], data["user"], data["password"],
                                "ls {}/{}".format(data["folder_ext2"], make_subfolder[0]), make_subfolder[1]))
    assert all(res)


def test_step7():
    assert ssh_checkout(data["host"], data["user"], data["password"], "7z d {}/arx1.7z".format(data["folder_out"]),
                        "Everything is Ok"), "Test7 Fail"
