from pwn import *
context.proxy = (socks.SOCKS5, "localhost", 1081)
context.arch='amd64'
r = remote('10.214.160.13',11002)
#一开始接受7行
r.recvlines(7)
a=eval(r.recvuntil(b"=").decode("utf-8")[:-2])
r.sendline(str(a).encode('utf-8'))
for i in range(9):
    r.recvlines(3)
    a=r.recvuntil(b"=").decode("utf-8")[:-2]
    r.sendline(str(eval(a)).encode('utf-8'))
r.interactive()
    

