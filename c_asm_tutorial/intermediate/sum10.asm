section .text
    global _start

_start:
    mov rcx, 10
    xor rax, rax       ; sum = 0

loop_start:
    add rax, rcx
    loop loop_start

    ; print result (assumes result < 256)
    add al, '0'
    mov [res], al
    mov rax, 1
    mov rdi, 1
    mov rsi, res
    mov rdx, 2
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall

section .bss
res resb 2
