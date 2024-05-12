import base64

hexstr = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytestr = bytes.fromhex(hexstr)
print(base64.b64encode(bytestr))
