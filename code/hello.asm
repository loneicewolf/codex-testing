section .data
fmt db "Hello, %s!", 10, 0
default_name db "world",0

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp
    mov rax, rdi    ; argc
    mov rbx, rsi    ; argv
    cmp rax, 2
    jl .use_default
    mov rdi, fmt
    mov rsi, [rbx+8] ; argv[1]
    xor eax, eax
    call printf
    jmp .done
.use_default:
    mov rdi, fmt
    mov rsi, default_name
    xor eax, eax
    call printf
.done:
    mov eax, 0
    leave
    ret
