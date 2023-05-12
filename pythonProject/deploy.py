from checkout import ssh_checkout
from load_file import upload_files


def deploy():
    res = []
    upload_files("0.0.0.0", "user22", "2222", "/home/user/p7zip-full.deb", "/home/user22/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user22", "2222", "echo '2222' | sudo -S dpkg -i /home/user22/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user22", "2222", "echo '2222' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
