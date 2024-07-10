import binascii

h = '49484452000001C2000029C0802000000'
b = bytes.fromhex(h)
c = binascii.crc32(b)
print(hex(c))
