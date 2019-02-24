section .data

msg db 'You have been hacked!', 0xa

section .text

global _start

start:

push rbp
mov rbp, rsp
lea rdi, qword[0x2004]
call sym.imp.puts
mov eax, 0
pop rbp
ret