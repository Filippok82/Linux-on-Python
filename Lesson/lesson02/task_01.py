import subprocess

result = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding="utf-8", stdout=subprocess.DEVNULL)
print(result.stdout)

result1 = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding="utf-8", stdout=subprocess.PIPE)
print(result1.stdout)

result2 = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding="utf-8", stderr=subprocess.STDOUT,\
                         stdout=subprocess.PIPE)
print(result2.stdout)
