; Minimal assembly wrapper calling C Dual_EC_DRBG
; nasm -felf64 dual_ec_drbg.asm && gcc dual_ec_drbg.o ../c/dual_ec_drbg.c -o dual_ec_drbg

section .text
    global main
    extern dual_ec_drbg

main:
    push rbp
    mov rbp, rsp
    mov edi, 7      ; seed
    mov esi, 5      ; blocks
    call dual_ec_drbg
    mov eax, 0
    pop rbp
    ret
