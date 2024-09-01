import re
def hex_to_binary_file(hex_data, output_file):
    byte_data = bytes.fromhex(hex_data)
    with open(output_file, 'wb') as bin_file:
        bin_file.write(byte_data)
    print(f"Data written to {output_file}")
find=''
with open('D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/dnscap.txt','r',encoding='utf-16') as f:
    for i in f:
        text = re.findall(r'([\w\.]+)\.skull',i)
        if text:
            find += text[0].replace('.','')
hex_to_binary_file(find,'D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/question')