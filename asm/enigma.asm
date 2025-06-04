section .data
    input db "HELLO",0
    rotor db "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor_inv db "UWYGADFPVZBECKMTHXSLRINQOJ"
    reflector db "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    output db 6 dup(0)
    fmt db "%s",10,0

section .text
    global main
    extern printf

main:
    push rbp
    mov rbp, rsp
    mov rsi, input
    mov rdi, output
    xor ecx, ecx ; rotor position
.loop:
    mov al, [rsi]
    test al, al
    je .done
    sub al, 'A'
    mov bl, cl
    add bl, al
    cmp bl, 26
    jb .step1
    sub bl, 26
    cmp bl, 26
    jb .step1
    sub bl, 26
.step1:
    movzx ebx, bl
    mov bl, [rotor+rbx]
    sub bl, 'A'
    movzx ebx, bl
    mov bl, [reflector+rbx]
    sub bl, 'A'
    movzx ebx, bl
    mov bl, [rotor_inv+rbx]
    sub bl, 'A'
    movzx ebx, bl
    cmp bl, cl
    jb .no_borrow
    sub bl, cl
    jmp .sub_done
.no_borrow:
    ; bl < cl, so add 26 before subtract
    add bl, 26
    sub bl, cl
.sub_done:
    cmp bl, 26
    jb .result
    sub bl, 26
.result:
    add bl, 'A'
    mov [rdi], bl
    inc rsi
    inc rdi
    inc cl
    cmp cl, 26
    jb .loop
    xor cl, cl
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
