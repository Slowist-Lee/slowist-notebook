import os
import binascii
import struct
misc = open("1.png","rb").read()
data = misc[12:16] + struct.pack('>i',)+ misc[20:29]
crc32 = binascii.crc32(data) & 0xffffffff
print(crc32)