import re
# import struct
# import time
def write_file(lines,output_file):
    with open(output_file,'w',encoding='utf-16') as output:
        output.writelines(lines)
    print("written file<{}>".format(output_file))
def hex_to_binary_file(hex_data, output_file):
    byte_data = bytes.fromhex(hex_data)
    with open(output_file, 'wb') as bin_file:
        bin_file.write(byte_data)
    print(f"Data written to {output_file}")

find = []

with open('D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/dnscap.txt','r',encoding='utf-16') as f:
    for i in f:
        text = re.findall(r'([\w\.]+)\.skull',i)
        if text:
            tmp = text[0].replace('.','')
            find.append(tmp[18:])
last=[]
for i in find:
    if i not in last:
        last.append(i)
last_string=''.join(last)
# write_file(last_string,'D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/question')
# bytes from hex
hex_data = last_string
output_file = "D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/output.bin"
hex_to_binary_file(hex_data, output_file)
print("written to output.bin")

