section .data
    usage db "Usage: ./filecat <file>\n",0

section .bss
    buf resb 1024

section .text
    global _start

_start:
    ; check argc
    mov rax, [rsp]
    cmp rax, 2
    je read_file

    ; print usage
    mov rax, 1
    mov rdi, 1
    mov rsi, usage
    mov rdx, 25
    syscall
    jmp exit

read_file:
    mov rdi, [rsp+16] ; argv[1]
    mov rax, 2        ; sys_open
    mov rsi, 0        ; O_RDONLY
    syscall
    mov r12, rax      ; store fd

read_loop:
    mov rax, 0        ; sys_read
    mov rdi, r12
    mov rsi, buf
    mov rdx, 1024
    syscall
    cmp rax, 0
    jle close_file
    mov r13, rax      ; bytes read

    mov rax, 1        ; sys_write
    mov rdi, 1
    mov rsi, buf
    mov rdx, r13
    syscall
    jmp read_loop

close_file:
    mov rax, 3        ; sys_close
    mov rdi, r12
    syscall

exit:
    mov rax, 60
    xor rdi, rdi
    syscall
