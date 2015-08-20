from Crypto.Hash import SHA256
import getpass

print(SHA256.new(getpass.getpass()).hexdigest())

