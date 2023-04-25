import time


def retry(func):
    def wrapper():
        try:
            func()
        except:
            print("retring...")
            time.sleep(1)
            func()

    return wrapper()


@retry
def might_fail():
    print("might fial")
    raise Exception


might_fail()
