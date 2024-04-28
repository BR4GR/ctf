chars = 'DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl'

def decrypt(encrypted_chars):
    lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
    lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

    out = ""
    prev = 0  # initial 'prev' value as in encryption

    for char in encrypted_chars:
        cur_in_lookup2 = lookup2.index(char)
        # Finding the matching 'cur' value in lookup1
        # This involves solving (cur - prev) % 40 == cur_in_lookup2 for 'cur'
        for cur in range(len(lookup1)):
            if (cur - prev) % 40 == cur_in_lookup2:
                out += lookup1[cur]
                prev = cur  # update prev to current for next iteration
                break

    return out

decrypted_message = decrypt(chars)
# print(decrypted_message)

#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print(chars[i]) #prints
        b += 1 / 1