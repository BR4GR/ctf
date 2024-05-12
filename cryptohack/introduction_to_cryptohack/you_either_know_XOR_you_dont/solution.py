from binascii import unhexlify
from pwn import xor
import string
import itertools

# I've encrypted the flag with my secret key, you'll never be able to guess it.
s = unhexlify('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

def generate_passwords(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for password in itertools.product(characters, repeat=length):
        yield ''.join(password)


for i in range(5):
    for password in generate_passwords(i):
        res = (xor(s, password)).decode()
        if "crypto" in res:
            print(res)
            break

