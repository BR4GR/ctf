from binascii import unhexlify
from pwn import xor

# I've encrypted the flag with my secret key, you'll never be able to guess it.
s: bytes = unhexlify('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
known_plaintext: bytes = b"crypto{"

key = xor(s[:len(known_plaintext) + 1], known_plaintext)
print(key)

key = b"myXORkey"
flag: str = xor(s, key).decode()
print(flag)

# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}

