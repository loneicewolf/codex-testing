section .data
    input db "HELLO WORLD",0
    shift db 3
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
.loop:
    mov al, [rsi]
    test al, al
    je .done
    cmp al, 'A'
    jb .copy
    cmp al, 'Z'
    ja .copy
    sub al, 'A'
    add al, [shift]
    cmp al, 26
    jl .nowrap
    sub al, 26
.nowrap:
    add al, 'A'
    jmp .store
.copy:
    mov al, [rsi]
.store:
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
