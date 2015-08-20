import getpass
from Crypto.Hash import SHA256


def load_password_hash():
    f = open('password-hash.txt', 'r')
    line = f.readline()
    f.close()
    return line


def check_password(clear_password, password_hash):
    hashed_result = SHA256.new(clear_password).hexdigest()
    return hashed_result == password_hash


def main(password):
    finished = False
    passed = 0
    failed = 0
    while not finished:
        line = getpass.getpass()
        if check_password(line, password):
            passed += 1
        elif line == 'q':
            pct = (passed/passed + failed) * 100
            print("Success vs. fail {0}/{1} ({2}% success)".format(passed, failed, (pct)))
            finished = True
        else:
            failed += 1


if __name__ == '__main__':
    hashed_password = load_password_hash()
    main(hashed_password)