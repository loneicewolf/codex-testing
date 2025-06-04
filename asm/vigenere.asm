; Simple Vigenere cipher demonstration

section .data
    input db "HELLO WORLD",0
    key db "KEY",0
    keylen equ 3
    output db 12 dup(0)
    fmt db "%s",10,0

section .text
    global main
    extern printf

main:
    push rbp
    mov rbp, rsp
    mov rsi, input
    mov rdi, output
    xor ecx, ecx
.loop:
    mov al, [rsi]
    test al, al
    je .done
    cmp al, 'A'
    jb .copy
    cmp al, 'Z'
    ja .copy
    sub al, 'A'
    mov bl, [key+rcx]
    sub bl, 'A'
    add al, bl
    cmp al, 26
    jl .nowrap
    sub al, 26
.nowrap:
    add al, 'A'
    inc ecx
    cmp ecx, keylen
    jl .store
    xor ecx, ecx
.store:
    mov [rdi], al
    inc rsi
    inc rdi
    jmp .loop
.copy:
    mov al, [rsi]
    mov [rdi], al
    inc rsi
    inc rdi
    jmp .loop
.done:
    mov byte [rdi], 0
    mov rdi, fmt
    mov rsi, output
    xor eax, eax
    call printf
    xor eax, eax
    leave
    ret
