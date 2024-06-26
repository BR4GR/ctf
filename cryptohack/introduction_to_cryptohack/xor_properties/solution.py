from binascii import unhexlify

KEY1 = unhexlify('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_1 = unhexlify('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_3 = unhexlify('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_KEY1_3_2 = unhexlify('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
# Before you XOR these objects, be sure to decode from hex to bytes.


def xor(l, r):
    res = bytes(i ^ j for i, j in zip(l, r))
    return res


KEY_1_2_3 = xor(KEY1, KEY2_3)
FLAG = xor(FLAG_KEY1_3_2, KEY_1_2_3)
print(FLAG.decode())
