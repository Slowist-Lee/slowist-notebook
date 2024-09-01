def extract_plte_data(file_path):
    with open(file_path, 'rb') as f:
        # Read the file in binary mode
        while True:
            # Read the length of the chunk (4 bytes)
            length_bytes = f.read(4)
            if len(length_bytes) < 4:
                # End of file
                break
            length = int.from_bytes(length_bytes, 'big')
            
            # Read the chunk type (4 bytes)
            chunk_type = f.read(4)
            if len(chunk_type) < 4:
                # End of file
                break
            
            # Check if the chunk type is 'PLTE'
            if chunk_type == b'PLTE':
                print("Found PLTE chunk")
                
                # Read the chunk data
                chunk_data = f.read(length)
                # Optionally, read the CRC (4 bytes)
                crc = f.read(4)
                
                return chunk_data
            
            else:
                # Skip over this chunk's data and CRC
                f.seek(length + 4, 1)
                
    raise ValueError("PLTE chunk not found")

# Example usage
try:
    hidden_data = extract_plte_data('D:/palette.png')
    print(f"PLTE data extracted: {hidden_data[:20]}...")  # Print first 20 bytes for brevity
except ValueError as e:
    print(e)
