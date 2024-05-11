import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
encrypted_flag = 'dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac'


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(text):
    decrypted = ""
    pairs = []
    while text:
        pairs.append(text[:2])
        text = text[2:]
    for pair in pairs:
        a, b = pair



def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshift(c, k):
    # Offset the letters in the opposite direction.
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    # Instead of moving forward through the alphabet, move backwards.
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


flag = "q"
key = "b"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])

print("flag:", flag)

print("b16:", b16)
print("enc:", enc)
unshifted = ""
for i, c in enumerate(enc):
    unshifted += unshift(c, key[i % len(key)])

print("unshifted:", unshifted)
