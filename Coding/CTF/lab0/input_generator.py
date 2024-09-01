import struct

def create_heartbeat_packet(size, timestamp, index, cred, data):
    packet = struct.pack('<IIII', size, timestamp, index, cred)
    packet += data.encode('utf-8')
    return packet

def main():
    size = 8 
    timestamp = 123456789  
    index = 1  
    cred = 42  
    data = "AAA"  

    packet = create_heartbeat_packet(size, timestamp, index, cred, data)
    with open("heartbeat_input.bin", "wb") as f:
        f.write(packet)
    print("Heartbeat packet written to 'heartbeat_input.bin'")
    print(f"Packet content: {packet}")

if __name__ == "__main__":
    main()
# import struct
# def create_heartbeat_packet(size, timestamp, index, cred, data):
#     # Pack the fixed part of the packet
#     packet = struct.pack('<IIII', size, timestamp, index, cred)
#     # Append the data part
#     packet += data.encode('utf-8')
#     return packet

# def main():
#     size = 21  # Example size (must be at least 16 + len(data))
#     timestamp = 123456789  # Example timestamp
#     index = 1  # Example index
#     cred = 42  # Example cred
#     data = "AAA"  # Example data

    
#     # Create the heartbeat packet
#     packet = create_heartbeat_packet(size, timestamp, index, cred, data)
    
#     # Write the packet to a file
#     with open("heartbeat_input.bin", "wb") as f:
#         f.write(packet)
    
#     print("Heartbeat packet written to 'heartbeat_input.bin'")
#     print(f"Packet content: {packet}")

# if __name__ == "__main__":
#     main()

# import struct

# def create_heartbeat_packet(size, timestamp, index, cred, data):
#     packet = struct.pack('<IIII', size, timestamp, index, cred)
#     packet += data.encode('utf-8')
#     # Add padding to reach the desired size
#     padding_length = size - len(packet)
#     if padding_length > 0:
#         packet += b'\x00' * padding_length
#     return packet

# def main():
#     size = 40  # Larger than the actual data length
#     timestamp = 123456789  # Example timestamp
#     index = 1  # Example index
#     cred = 42  # Example cred
#     data = "AAA"  # Example data

#     # Create the heartbeat packet
#     packet = create_heartbeat_packet(size, timestamp, index, cred, data)
#     # Write the packet to a file
#     with open("heartbeat_input.bin", "wb") as f:
#         f.write(packet)
#     print("Heartbeat packet written to 'heartbeat_input.bin'")
#     print(f"Packet content: {packet}")

# if __name__ == "__main__":
#     main()


