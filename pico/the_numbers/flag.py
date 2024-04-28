from string import ascii_uppercase

nubers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14,'}']

flag = []
for n in nubers:
    if isinstance (n,int):
        flag.append(ascii_uppercase[n-1])
    else:
        flag.append(n)

print(''.join(flag))