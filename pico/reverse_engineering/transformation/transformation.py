with open("enc", "r+") as file1:
    enc_flag = file1.read()


def encrypt(flag):
    "".join(
        [chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]
    )


ret = ""
for e in enc_flag:
    num = hex(ord(e))
    chars = bytearray.fromhex(num.lstrip("0x")).decode()
    ret += chars

print(ret)

print(hex(ord("p")))
print(hex(ord("p") << 8))
