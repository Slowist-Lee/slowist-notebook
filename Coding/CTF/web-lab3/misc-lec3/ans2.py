def hex_to_binary_file(hex_data, output_file):
    byte_data = bytes.fromhex(hex_data)
    with open(output_file, 'wb') as bin_file:
        bin_file.write(byte_data)
    print(f"Data written to {output_file}")
output.bin
hex_to_binary_file(final_s, 'D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/image')

# import struct

# def read_chunk(f):
#     length_bytes = f.read(4)
#     if len(length_bytes) == 0:
#         return None, None, None, None  # 文件结束
#     length = struct.unpack('>I', length_bytes)[0]
#     chunk_type_bytes = f.read(4)
#     if len(chunk_type_bytes) != 4:
#         return length, None, None, None  # 数据块类型读取失败
#     chunk_type = chunk_type_bytes.decode('ascii')
#     data = f.read(length)
#     crc = f.read(4)
#     return length, chunk_type, data, crc

# def parse_png(file_path):
#     with open(file_path, 'rb') as f:
#         # 检查文件签名
#         signature = f.read(8)
#         if signature != b'\x89PNG\r\n\x1a\n':
#             raise ValueError("Not a valid PNG file")

#         chunks = []
#         while True:
#             length, chunk_type, data, crc = read_chunk(f)
#             if length is None or chunk_type is None:
#                 break
#             chunk = (chunk_type, length, data, crc)
#             if chunk not in chunks:
#                 chunks.append(chunk)
#             if chunk_type == 'IEND':
#                 break

#         return signature, chunks

# def write_png(signature, chunks, output_path):
#     with open(output_path, 'wb') as f:
#         # 写入文件签名
#         f.write(signature)
#         for chunk_type, length, data, crc in chunks:
#             # 写入长度字段
#             f.write(struct.pack('>I', length))
#             # 写入类型字段
#             f.write(chunk_type.encode('ascii'))
#             # 写入数据部分
#             f.write(data)
#             # 写入CRC字段
#             f.write(crc)

# def main():
#     input_path = 'D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/extracted'
#     output_path = 'D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/output_final'
#     signature, png_chunks = parse_png(input_path)
#     write_png(signature, png_chunks, output_path)
#     print("PNG file processed and saved to", output_path)
# main()
# # chunks=[]

# # def read_chunk(f):
# #     length_bytes = f.read(4)
# #     if len(length_bytes) == 0:
# #         return None, None, None, None  # 文件结束
# #     length = struct.unpack('>I', length_bytes)[0]
# #     # 读取类型字段
# #     chunk_type = f.read(4).decode('ascii')
# #     # 读取数据部分
# #     data = f.read(length)
# #     # 读取CRC字段
# #     crc = f.read(4)
# #     return length, chunk_type, data, crc

# # def write_png(signature, chunks, output_path):
# #     with open(output_path, 'wb') as f:
# #         # 写入文件签名
# #         f.write(signature)
# #         for chunk_type, length, data, crc in chunks:
# #             # 写入长度字段
# #             f.write(struct.pack('>I', length))
# #             # 写入类型字段
# #             f.write(chunk_type.encode('ascii'))
# #             # 写入数据部分
# #             f.write(data)
# #             # 写入CRC字段
# #             f.write(crc)
# #     print("PNG file processed and saved to", output_path)

# # p+=8 #skip signature
# # while True:
# #     length, chunk_type, data, crc = read_chunk(f)
# #     # if length is None:
# #     #     break
# #     chunk=[]
# #     chunk.append(chunk_type)
# #     chunk.append(length)
# #     chunk.append(data)
# #     chunk.append(crc)
# #     if chunk not in chunks:
# #         chunks.append(chunk)
# #     if chunk_type=='IEND':
# #         break
# # print("png ended")
# # signature = b'\x89PNG\r\n\x1a\n'
# # write_png(signature, chunks, "D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/output_final")


