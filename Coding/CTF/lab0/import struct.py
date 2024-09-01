import struct
import subprocess
import time

def create_packet(size, data):
    pkt_format = 'I' + str(len(data)) + 's'
    return struct.pack(pkt_format, size, data.encode())
proc = subprocess.Popen(['./program'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
try:
    for _ in range(1000):
        packet = create_packet(20, "A" * 16)  
        proc.stdin.write(packet)
        proc.stdin.flush()
        time.sleep(0.1)  
except BrokenPipeError:
    print("Detected a crash: Broken pipe")

proc.stdin.close()
proc.wait()

if proc.returncode != 0:
    print(f"crash with code: {proc.returncode}")
else:
    print("smooth")
