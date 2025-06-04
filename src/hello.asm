section .data
    msg db "Hello from Assembly!", 10
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1         ; sys_write
    mov rdi, 1         ; file descriptor (stdout)
    mov rsi, msg       ; pointer to message
    mov rdx, len       ; message length
    syscall

    mov rax, 60        ; sys_exit
    xor rdi, rdi       ; exit code 0
    syscall
