import gzip

# 输入和输出文件路径
input_file_path = 'D:/MyRepository/slowist-notebook/docs/Coding/CTF/chalreal.zlib'
output_file_path = 'D:/MyRepository/slowist-notebook/docs/Coding/CTF/chaloutput'


# 读取压缩文件并解压缩
with gzip.open(input_file_path, 'rb') as compressed_file:
    decompressed_data = compressed_file.read()

# 写入解压后的数据到输出文件
with open(output_file_path, 'wb') as output_file:
    output_file.write(decompressed_data)

print("解压缩完成")
