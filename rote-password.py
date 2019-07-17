import getpass

from Crypto.Hash import SHA256
from colorama import init, deinit, Fore


def load_password_hash():
    f = open('password-hash.txt', 'r')
    line = f.readline()
    f.close()
    return line.strip()


def check_password(clear_password, password_hash):
    hashed_result = SHA256.new(clear_password).hexdigest()
    return hashed_result == password_hash


def main(expected):
    finished = False
    success = 0
    fail = 0
    while not finished:
        actual = getpass.getpass()

        if check_password(actual, expected):
            success += 1
            display_result(Fore.GREEN, "Correct", success, fail)
        elif actual == 'q':
            finished = True
            print(Fore.RESET + "Quit")
        else:
            fail += 1
            display_result(Fore.RED, "Incorrect", success, fail)
        print(Fore.WHITE + '')


def display_result(color, msg, success, fail):
    pct = round((float(success) / float(success + fail)) * 100.0, 1)
    print(color + "{0}: {1}/{2} ({3}% success)".format(msg, success, fail, pct))


if __name__ == '__main__':
    init()
    hashed_password = load_password_hash()
    main(hashed_password)
    deinit()
