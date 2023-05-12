import yaml

from checkout import ssh_checkout_negative

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(make_bad_arx):
    # test1
    assert ssh_checkout_negative(data["host"], data["user"], data["password"],
                                 "d {}; 7z e {} -o{} -y".format(data["folder_out"], data["path_arx"],
                                                                data["folder_ext"]),
                                 "ERROR"), "Test4 Fail"


def test_step2(make_bad_arx):
    # test2
    assert ssh_checkout_negative(data["host"], data["user"], data["password"],
                                 "cd {}; 7z t {}".format(data["folder_out"], data["path_arx"]), "ERROR"), "Test5 Fail"
