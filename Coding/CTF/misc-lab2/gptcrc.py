import binascii

def calculate_crc_from_ihdr(data):
    # IHDR数据块的长度字段（4字节）加上类型字段（4字节）
    ihdr_chunk_length = 4 + 4
    # IHDR数据块的数据长度固定为13字节
    ihdr_data_length = 13

    # 确保数据长度足够
    if len(data) < ihdr_chunk_length + ihdr_data_length:
        raise ValueError("Data length is insufficient to contain IHDR chunk")

    # 提取IHDR数据块的类型和数据（不包括CRC字段）
    ihdr_chunk_type_and_data = data[4:ihdr_chunk_length + ihdr_data_length]

    # 计算CRC
    crc = binascii.crc32(ihdr_chunk_type_and_data) & 0xffffffff

    return crc

# 示例数据，替换为你的实际数据
# 例如：长度字段(4字节) + 类型字段(4字节) + 数据字段(13字节)
data = b'\x00\x00\x00\x0D' + b'IHDR' + b'\x00\x00\x01\xC2\x00\x00\x01\x2C\x08\x02\x00\x00\x00'

# 计算IHDR数据块的CRC校验码
crc = calculate_crc_from_ihdr(data)
print(f'IHDR数据块的CRC校验码: {crc:08X}')
