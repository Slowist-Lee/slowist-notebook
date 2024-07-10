import struct

def read_png_ihdr(file_path):
    with open(file_path, 'rb') as f:
        # 跳过 PNG 文件头（8 字节）
        f.seek(8)
        
        # 读取 IHDR 块长度（4 字节）和类型（4 字节）
        ihdr_length = struct.unpack('>I', f.read(4))[0]
        ihdr_type = f.read(4)
        
        if ihdr_type != b'IHDR':
            raise ValueError("Invalid PNG file: missing IHDR chunk")
        
        # 读取 IHDR 块内容（13 字节）
        ihdr_data = f.read(13)
        
        # 解析 IHDR 块内容
        width, height, bit_depth, color_type, compression, filter_method, interlace_method = struct.unpack('>IIBBBBB', ihdr_data)
        
        print(f"Width: {width}")
        print(f"Height: {height}")
        print(f"Bit Depth: {bit_depth}")
        print(f"Color Type: {color_type}")
        print(f"Compression Method: {compression}")
        print(f"Filter Method: {filter_method}")
        print(f"Interlace Method: {interlace_method}")

# 示例使用
read_png_ihdr('1.png')
