import struct
def create_heartbeat_packet(size, timestamp, index, cred, data):
    packet = struct.pack('<IIII', size, timestamp, index, cred)
    packet += data.encode('utf-8')
    return packet

def main():
    size = 616  
    timestamp = 123456789 
    index = 1  
    cred = 42 
    data = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  
    
      # 600*'A' it can't be viewed :(

    
  
    packet = create_heartbeat_packet(size, timestamp, index, cred, data)
    
    with open("heartbeat_input.bin", "wb") as f:
        f.write(packet)
    
    print("Heartbeat packet written to 'heartbeat_input.bin'")
    print(f"Packet content: {packet}")

if __name__ == "__main__":
    main()