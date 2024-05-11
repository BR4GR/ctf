a = 88
b = 26
cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]
key = 35


# back to semi_cipher
semi_cipher = []
for c in cipher:
    semi_cipher.append(c // (key * 311))

print(semi_cipher)

# back to plain text
text_key="trudeau"
plain_text = ""
key_length = len(text_key)
for i, each in enumerate(semi_cipher):
    key_char = text_key[i % key_length]
    plain_text += chr(each ^ ord(key_char))
print(plain_text[::-1])