i = 13
l = 'label'

letters =[chr(ord(x) ^ i) for x in l]
res = "".join(letters)
print(f"crypto{{{res}}}")