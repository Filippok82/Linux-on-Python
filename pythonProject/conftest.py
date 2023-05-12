from datetime import datetime
import random
import string
import pytest
import yaml

from checkout import checkout_positive, ssh_checkout
from checkers import getout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return ssh_checkout(data["host"], data["user"], data["password"],
                        "mkdir {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                   data["folder_ext2"]), "")


@pytest.fixture()
def clear_folders():
    return ssh_checkout(data["host"], data["user"], data["password"],
                        "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                            data["folder_ext2"]), "")


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
                                                                                               filename), ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not ssh_checkout(data["host"], data["user"], data["password"],
                        "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
                                                                                                  subfoldername,
                                                                                                  testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx():
    ssh_checkout(data["host"], data["user"], data["password"], "cd {}; 7z a {}/arxbad -t{}".format(data["folder_in"],
                                                                                                   data["folder_out"],
                                                                                                   data["expansion"]),
                 "Everything is Ok")
    ssh_checkout(data["host"], data["user"], data["password"], "truncate -s 1 {}/arxbad.{}".format(data["folder_out"],
                                                                                                   data["expansion"]),
                 "Everything is Ok")
    yield "arxbad"
    ssh_checkout(data["host"], data["user"], data["password"],
                 "rm -f {}/arxbad.{}".format(data["folder_out"], data["expansion"]), "")



@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture()
def save_log(start_time, name=data["path_journal"]):
    with open(name, 'w') as f:
        f.write(getout("sudo journalctl --since '{}'".format(start_time)))
