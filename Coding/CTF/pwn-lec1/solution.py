from pwn import *
from wstube import websocket
context.proxy = (socks.SOCKS5, "localhost", 1081)
context.log_level= 'DEBUG'
context.arch = 'amd64'
p= websocket("wss://ctf.zjusec.com/api/proxy/065bb806-2e62-43c6-a12a-f1b47d37e60a")

p.sendafter(b"Request-1:give me code that performing ADD")
add_code=b"\xf3\x0f\x1e\xfa\x8d\x04\x37\xc3"
# Request-1: give me code that performing ADD
p.sendafter(b"Request-2:give me code that performing SUB")
add_code=b"\xf3\x0f\x1e\xfa\x89\xf8\x29\xf0\xc3"
# Request-2: give me code that performing SUB
p.sendafter(b"Request-3: give me code that performing AND")
add_code=b"\xf3\x0f\x1e\xfa\x89\xf8\x21\xf0\xc3"
# Request-3: give me code that performing AND
p.sendafter(b"Request-2:give me code that performing OR")
add_code=b"\xf3\x0f\x1e\xfa\x89\xf8\x09\xf0\xc3"
# Request-4: give me code that performing OR
p.sendafter(b"Request-5:give me code that performing XOR")
add_code=b"\xf3\x0f\x1e\xfa\x89\xf8\x31\xf0\xc3"
# Request-5: give me code that performing XOR
p.interactive()
