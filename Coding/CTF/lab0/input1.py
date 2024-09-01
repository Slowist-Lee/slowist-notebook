import struct
import subprocess

def create_normal_packet():
    size = 32  
    timestamp = 12345678
    index = 1
    cred = 0
    data = "A" * 16  
    pkt_format = 'I I I I ' + str(len(data)) + 's'  
    return struct.pack(pkt_format, size, timestamp, index, cred, data.encode())

def create_complete_input():
    pkt1 = create_normal_packet()
    data_size = 32 - 16  
    data = "A" * data_size  
    return pkt1 + data.encode()

proc = subprocess.Popen(
    ['./program'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

try:
    complete_input = create_complete_input()
    proc.stdin.write(complete_input)
    proc.stdin.flush()
    print("Packet sent, waiting for output...")

    output, error = proc.communicate(timeout=10)  
    proc.stdin.close()
    
    if proc.returncode != 0:
        print(f"Program crashed with return code: {proc.returncode}")
        print(f"Error output: {error.decode()}")
    else:
        print("Program did not crash")
        print(f"Program output: {output.decode()}")

except subprocess.TimeoutExpired:
    print("Program timeout, terminating process...")
    proc.kill()
    output, error = proc.communicate()
    print(f"Error output: {error.decode()}")

finally:
    proc.stdin.close()
    proc.wait()
