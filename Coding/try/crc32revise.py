import zipfile
import zlib
import struct

def update_crc(zip_path):
    with open(zip_path, 'rb+') as f:
        zip_file = zipfile.ZipFile(f)
        for zip_info in zip_file.infolist():
            f.seek(zip_info.header_offset)
            
            # Read the local file header
            local_file_header = f.read(30)
            filename_len = struct.unpack('<H', local_file_header[26:28])[0]
            extra_field_len = struct.unpack('<H', local_file_header[28:30])[0]
            filename = f.read(filename_len)
            extra_field = f.read(extra_field_len)

            # Read the file data
            compressed_data = f.read(zip_info.compress_size)
            
            # Decompress the data if needed
            if zip_info.compress_type == zipfile.ZIP_DEFLATED:
                decompressed_data = zlib.decompress(compressed_data, -15)
            else:
                decompressed_data = compressed_data
            
            # Calculate the CRC32 checksum of the decompressed data
            crc32 = zlib.crc32(decompressed_data) & 0xffffffff
            
            # Update the CRC32 value in the central directory header
            f.seek(zip_info.header_offset + 14)
            f.write(struct.pack('<L', crc32))
            
            # Update the CRC32 value in the local file header
            central_directory_offset = zip_info.header_offset + 30 + filename_len + extra_field_len + zip_info.file_size
            f.seek(central_directory_offset + 16)
            f.write(struct.pack('<L', crc32))
            
        zip_file.close()

# Example usage
zip_path = input()
update_crc(zip_path)
print(f"Updated CRC checksum for {zip_path}")
