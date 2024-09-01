import binascii
import struct

def calculate_crc(data):
    """计算数据的CRC32校验码"""
    return binascii.crc32(data) & 0xffffffff

def update_crc_in_file(file_path, crc_position, start_pos, num_bytes):
    """更新文件中的CRC32校验码"""
    with open(file_path, 'r+b') as f:
        # 移动文件指针到 start_pos 并读取 num_bytes 个字节
        f.seek(start_pos)
        data = f.read(num_bytes)

        # 计算新的CRC32校验码
        new_crc = calculate_crc(data)
        
        # 将文件指针移动到CRC32校验码的位置
        f.seek(crc_position)
        datanew=f.read(4)
        hex_data=list(datanew)
        for i in range(len(hex_data)):
            hex_data[i]=hex(hex_data[i])[2:]
        print(hex_data)
        # 写入新的CRC32校验码
        f.write(struct.pack('<L', new_crc))

        print(f'Updated CRC32 checksum to: {new_crc:08X}')

# 示例用法
file_path = 'test.zip'
crc_position = 14  # CRC32 校验码的位置，假设为14
start_pos = 10  # 从第10位开始读取
num_bytes = 14  # 读取14个字节

update_crc_in_file(file_path, crc_position, start_pos, num_bytes)
