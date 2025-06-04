; Simple x86-64 assembly program to brute force Caesar cipher
; nasm -felf64 caesar.asm && ld caesar.o -o caesar

section .data
    prompt db "Ciphertext: ", 0

section .bss
    buf resb 256

section .text
    global _start

_start:
    ; print prompt
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, 11
    syscall

    ; read input
    mov rax, 0
    mov rdi, 0
    mov rsi, buf
    mov rdx, 256
    syscall
    mov rbx, rax ; length

    xor rcx, rcx ; shift
next_shift:
    mov rdi, buf
    mov rsi, rbx
    call print_shift
    inc rcx
    cmp rcx, 26
    jl next_shift

    mov rax, 60
    xor rdi, rdi
    syscall

print_shift:
    push rbx
    push rcx
    mov rax, 1
    mov rdi, 1
    mov rdx, rbx
.loop:
    mov al, byte [rdi+rsi-1]
    cmp al, 'A'
    jb .write
    cmp al, 'Z'
    ja .write
    sub al, 'A'
    sub al, cl
    add al, 26
    mov bl, 26
    div bl
    add al, 'A'
.write:
    mov byte [rdi+rsi-1], al
    dec rdx
    jnz .loop
    mov rax, 1
    mov rdi, 1
    mov rsi, buf
    mov rdx, rbx
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall
    pop rcx
    pop rbx
    ret

section .data
    newline db 10
