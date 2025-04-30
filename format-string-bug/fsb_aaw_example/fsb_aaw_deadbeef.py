from pwn import *
def slog(name, addr): return success(': '.join([name, hex(addr)]))

context.log_level = 'debug'

p = process('./fsb_aaw_example')

p.recvuntil(b"`secret`: ")
secret = int(p.recvline()[2:-1], 16)


