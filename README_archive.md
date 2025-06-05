<div align="center">
# Repository Source Archive
</div>

This README assembles every file from the repository for reference and study.

> **AI-Generated Content Notice**
> This document was created with help from AI tools. It is provided as-is for academic and research use only. No warranty is expressed or implied, and the authors assume no liability.


## Table of Contents
- [README.md](#READMEmd)
- [asm/README.md](#asmREADMEmd)
- [asm/caesar.asm](#asmcaesarasm)
- [asm/dual_ec_drbg.asm](#asmdual_ec_drbgasm)
- [bash/README.md](#bashREADMEmd)
- [bash/aliases.sh](#bashaliasessh)
- [bash/analyze.sh](#bashanalyzesh)
- [bash/dual_ec_drbg.sh](#bashdual_ec_drbgsh)
- [bash/net_utils.sh](#bashnet_utilssh)
- [c/Makefile](#cMakefile)
- [c/README.md](#cREADMEmd)
- [c/ciphers.c](#cciphersc)
- [c/ciphers.h](#cciphersh)
- [c/dual_ec_drbg.c](#cdual_ec_drbgc)
- [c/main.c](#cmainc)
- [code/hello.asm](#codehelloasm)
- [code/hello.c](#codehelloc)
- [code/hello.py](#codehellopy)
- [paper.tex](#papertex)
- [python/README.md](#pythonREADMEmd)
- [python/analyze.py](#pythonanalyzepy)
- [python/dual_ec_drbg.py](#pythondual_ec_drbgpy)
- [python/insecure_rng.py](#pythoninsecure_rngpy)
- [python/secure_rng.py](#pythonsecure_rngpy)
- [references.bib](#referencesbib)

---
<a name="READMEmd"></a>
### README.md
<details>
<summary>Show README.md</summary>
```markdown
# NOT MY CODE!
# ITS AI ASSISTED (GPT,CODEX,AI,OPENAI)
:)

# Cipher Analysis Examples

This repository now includes simple cipher analysis tools in four languages:

- `python/`: command line utilities for Caesar, Vigenère, a simplified Enigma simulator, and RNG demonstrations (insecure and secure).
- `c/`: minimal CLI tool demonstrating Caesar and Vigenère breaking.
- `asm/`: x86-64 assembly program to brute force Caesar.
- `bash/`: shell script performing basic Caesar and Vigenère operations.

Each directory contains a README with usage examples.
```
</details>

<a name="asmREADMEmd"></a>
### asm/README.md
<details>
<summary>Show asm/README.md</summary>
```markdown
# Assembly Caesar Breaker

An example x86-64 assembly program that prints all 26 shifts of a Caesar cipher.

```
nasm -felf64 caesar.asm
ld caesar.o -o caesar
./caesar
```
```
</details>

<a name="asmcaesarasm"></a>
### asm/caesar.asm
<details>
<summary>Show asm/caesar.asm</summary>
```asm
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
```
</details>

<a name="asmdual_ec_drbgasm"></a>
### asm/dual_ec_drbg.asm
<details>
<summary>Show asm/dual_ec_drbg.asm</summary>
```asm
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
```
</details>

<a name="bashREADMEmd"></a>
### bash/README.md
<details>
<summary>Show bash/README.md</summary>
```markdown
# Bash Utilities

This directory contains helper scripts and useful shell functions.

## Cipher examples

`analyze.sh` provides quick Caesar and Vigenère operations:

```bash
./analyze.sh caesar "OLSSV DVYSK"
./analyze.sh vigenere "LXFOPVEFRNHR" KEY
```

## Aliases

`aliases.sh` defines a set of handy functions:

- `grep_ips` – extract unique IPv4 addresses from files or standard input.
- `grep_urls` – extract URLs from text streams.
- `grep_firefox_bookmarks PROFILE` – print bookmark URLs from a Firefox profile directory.
- `grep_edge_bookmarks PROFILE` – print bookmark URLs from a Microsoft Edge profile directory.
- `alert COLOR MESSAGE` – display a colored alert message similar to PowerShell's `Write-Host`.
`net_utils.sh` contains additional networking helpers:

- `grep_ipv4` – IPv4 extraction based on a regex from Stack Overflow.
- `grep_ipv6` – IPv6 extraction referencing discussions around `ip(7)`.
- `grep_urls` – improved URL matching inspired by cURL documentation.
- `ssl_subjects FILE...` – print certificate subjects via OpenSSL.
- `firefox_bookmarks PROFILE` – query bookmarks with sqlite3.
- `edge_bookmarks PROFILE` – parse Microsoft Edge bookmark files.


Source the file in your shell to make the functions available:

```bash
source aliases.sh
source net_utils.sh  # load the network helpers
```
```
</details>

<a name="bashaliasessh"></a>
### bash/aliases.sh
<details>
<summary>Show bash/aliases.sh</summary>
```bash
# Bash aliases for network log extraction and alerts

# Extract unique IPv4 addresses from input or files
grep_ips() {
    grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' "$@" | sort -u
}

# Extract unique URLs from input or files
grep_urls() {
    grep -Eio "(https?|ftp)://[^ \"'<>]+" "$@" | sort -u
}

# Dump bookmarks from a Firefox profile directory using sqlite3
# Usage: grep_firefox_bookmarks ~/.mozilla/firefox/XXXX.default-release
grep_firefox_bookmarks() {
    profile="$1"
    sqlite3 "$profile/places.sqlite" 'SELECT url FROM moz_places' 2>/dev/null
}

# Dump bookmarks from a Microsoft Edge profile directory
# Usage: grep_edge_bookmarks ~/.config/microsoft-edge/Default
grep_edge_bookmarks() {
    profile="$1"
    if [ -f "$profile/Bookmarks" ]; then
        grep -o '"url": "[^"]*"' "$profile/Bookmarks" | cut -d '"' -f4
    fi
}

# Display a colored alert message
# alert red "Something went wrong"
alert() {
    color=$1; shift
    message="$*"
    case $color in
        red) code='\e[31m' ;;
        green) code='\e[32m' ;;
        yellow) code='\e[33m' ;;
        blue) code='\e[34m' ;;
        magenta) code='\e[35m' ;;
        cyan) code='\e[36m' ;;
        blink) code='\e[5m' ;;
        *) code='\e[0m' ;;
    esac
    echo -e "\e[1m${code}${message}\e[0m"
}
```
</details>

<a name="bashanalyzesh"></a>
### bash/analyze.sh
<details>
<summary>Show bash/analyze.sh</summary>
```bash
#!/bin/bash

command=$1
text=$2

alphabet=ABCDEFGHIJKLMNOPQRSTUVWXYZ

caesar_break() {
    for shift in {0..25}; do
        result=""
        for ((i=0;i<${#text};i++)); do
            char=${text:i:1}
            idx=$(expr index "$alphabet" "${char^^}")
            if [ $idx -gt 0 ]; then
                idx=$(( (idx - 1 - shift + 26) % 26 ))
                result+=${alphabet:idx:1}
            else
                result+=$char
            fi
        done
        echo "$shift: $result"
    done
}

vigenere_decrypt() {
    key=$3
    keylen=${#key}
    result=""
    k=0
    for ((i=0;i<${#text};i++)); do
        char=${text:i:1}
        idx=$(expr index "$alphabet" "${char^^}")
        if [ $idx -gt 0 ]; then
            shift=$(expr index "$alphabet" "${key:k:1}")
            shift=$((shift - 1))
            idx=$(( (idx - 1 - shift + 26) % 26 ))
            result+=${alphabet:idx:1}
            k=$(( (k + 1) % keylen ))
        else
            result+=$char
        fi
    done
    echo "$result"
}

case $command in
    caesar)
        caesar_break
        ;;
    vigenere)
        vigenere_decrypt "$text" "$3"
        ;;
    *)
        echo "Usage: $0 {caesar|vigenere} TEXT [KEY]"
        ;;
esac
```
</details>

<a name="bashdual_ec_drbgsh"></a>
### bash/dual_ec_drbg.sh
<details>
<summary>Show bash/dual_ec_drbg.sh</summary>
```bash
#!/bin/bash
# Pure bash Dual_EC_DRBG demo with small curve
p=233
A=1
Px=3
Py=65
Qx=83
Qy=97
seed=${1:-7}
blocks=${2:-5}

inv_mod() {
  local a=$1
  local p=$2
  for ((i=1;i<p;i++)); do
    if (( (a*i) % p == 1 )); then
      echo $i
      return
    fi
  done
}

add_point() {
  local x1=$1 y1=$2 x2=$3 y2=$4
  if (( x1 == -1 )); then echo "$x2 $y2"; return; fi
  if (( x2 == -1 )); then echo "$x1 $y1"; return; fi
  if (( x1==x2 && (y1 + y2) % p == 0 )); then
    echo "-1 0"
    return
  fi
  local m
  if (( x1==x2 && y1==y2 )); then
    local denom=$(( (2*y1) % p ))
    local inv=$(inv_mod $denom $p)
    m=$(( (3*x1*x1 + A)*inv % p ))
  else
    local denom=$(( (x2 - x1 + p) % p ))
    local inv=$(inv_mod $denom $p)
    m=$(( ( (y2 - y1 + p) % p ) * inv % p ))
  fi
  local x3=$(( (m*m - x1 - x2) % p ))
  if (( x3 < 0 )); then x3=$((x3+p)); fi
  local y3=$(( (m*(x1 - x3) - y1) % p ))
  if (( y3 < 0 )); then y3=$((y3+p)); fi
  echo "$x3 $y3"
}

mul_point() {
  local k=$1 x=$2 y=$3
  local hx=-1 hy=0
  while (( k>0 )); do
    if (( k & 1 )); then
      read hx hy <<<$(add_point $hx $hy $x $y)
    fi
    read x y <<<$(add_point $x $y $x $y)
    k=$((k>>1))
  done
  echo "$hx $hy"
}

for ((i=0;i<blocks;i++)); do
  read sx sy <<<$(mul_point $seed $Px $Py)
  seed=$sx
  read rx ry <<<$(mul_point $seed $Qx $Qy)
  echo $rx
  seed=$sx
done
```
</details>

<a name="bashnet_utilssh"></a>
### bash/net_utils.sh
<details>
<summary>Show bash/net_utils.sh</summary>
```bash
# Convenient shell functions for extracting network related data
#
# These helpers were inspired by examples from Stack Overflow and the grep manual.
# They demonstrate good shell style: quoting variables, using regex with -E, and
# separating parsing from presentation.

# Extract unique IPv4 addresses from files or stdin
# Regex adapted from https://stackoverflow.com/a/36760050
grep_ipv4() {
    grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' "$@" | sort -u
}

# Extract unique IPv6 addresses. See ipv6 regex discussion:
# https://stackoverflow.com/questions/53497/regular-expression-that-matches-valid-ipv6-addresses
grep_ipv6() {
    grep -Eio '([0-9a-f]{0,4}:){2,7}[0-9a-f]{0,4}' "$@" | sed 's/%.*//' | sort -u
}

# Extract all URLs from input. Based on RFC 3986 and various blog posts.
# For details see: https://daniel.haxx.se/blog/2010/06/11/url-syntax/
grep_urls() {
    grep -Eio '(https?|ftp)://[^\"'"'"' <>]+' "$@" | sort -u
}

# Output subjects of SSL certificates found in PEM files
# Uses openssl x509 from OpenSSL documentation.
ssl_subjects() {
    for f in "$@"; do
        openssl x509 -noout -subject -in "$f" 2>/dev/null
    done
}

# Dump bookmark URLs from a Firefox profile directory
# Uses sqlite3 queries documented on Mozilla Support.
# Usage: firefox_bookmarks ~/.mozilla/firefox/XXXX.default-release
firefox_bookmarks() {
    profile="$1"
    sqlite3 "$profile/places.sqlite" 'SELECT url FROM moz_places' 2>/dev/null
}

# Dump bookmark URLs from a Microsoft Edge profile directory
# The JSON layout is described on various blog posts.
# Usage: edge_bookmarks ~/.config/microsoft-edge/Default
edge_bookmarks() {
    profile="$1"
    if [ -f "$profile/Bookmarks" ]; then
        grep -o '"url":\s*"[^"]*"' "$profile/Bookmarks" | cut -d '"' -f4
    fi
}
```
</details>

<a name="cMakefile"></a>
### c/Makefile
<details>
<summary>Show c/Makefile</summary>
```
CC=gcc
CFLAGS=-Wall -O2

all: cipher_tool

cipher_tool: main.o ciphers.o
	$(CC) $(CFLAGS) -o cipher_tool main.o ciphers.o

main.o: main.c ciphers.h
	$(CC) $(CFLAGS) -c main.c

ciphers.o: ciphers.c ciphers.h
	$(CC) $(CFLAGS) -c ciphers.c

clean:
	rm -f *.o cipher_tool
```
</details>

<a name="cREADMEmd"></a>
### c/README.md
<details>
<summary>Show c/README.md</summary>
```markdown
# C Cipher Analysis

A minimal CLI program to experiment with Caesar and Vigenere cipher breaking.

```
make
./cipher_tool caesar "L ORYH FLSKHUV"
./cipher_tool vigenere "LXFOPVEFRNHR" 3
```
```
</details>

<a name="cciphersc"></a>
### c/ciphers.c
<details>
<summary>Show c/ciphers.c</summary>
```c
#include <stdio.h>
#include <string.h>
#include "ciphers.h"

void caesar_break(const char *ciphertext) {
    for (int shift = 0; shift < 26; ++shift) {
        for (const char *p = ciphertext; *p; ++p) {
            if (*p >= 'A' && *p <= 'Z')
                putchar('A' + (*p - 'A' - shift + 26) % 26);
            else if (*p >= 'a' && *p <= 'z')
                putchar('a' + (*p - 'a' - shift + 26) % 26);
            else
                putchar(*p);
        }
        printf("\n");
    }
}

void vigenere_break(const char *ciphertext, int key_length) {
    size_t len = strlen(ciphertext);
    char key[key_length + 1];
    for (int i = 0; i < key_length; ++i) {
        int counts[26] = {0};
        for (size_t j = i; j < len; j += key_length) {
            char c = ciphertext[j];
            if (c >= 'A' && c <= 'Z')
                counts[c - 'A']++;
        }
        int max = 0, idx = 0;
        for (int k = 0; k < 26; ++k) {
            if (counts[k] > max) {
                max = counts[k];
                idx = k;
            }
        }
        key[i] = 'A' + (idx - ('E' - 'A') + 26) % 26;
    }
    key[key_length] = '\0';
    printf("Estimated key: %s\n", key);
}
```
</details>

<a name="cciphersh"></a>
### c/ciphers.h
<details>
<summary>Show c/ciphers.h</summary>
```c
#ifndef CIPHERS_H
#define CIPHERS_H

void caesar_break(const char *ciphertext);
void vigenere_break(const char *ciphertext, int key_length);

#endif // CIPHERS_H
```
</details>

<a name="cdual_ec_drbgc"></a>
### c/dual_ec_drbg.c
<details>
<summary>Show c/dual_ec_drbg.c</summary>
```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define P_FIELD 233
#define A_COEFF 1

typedef struct {
    int64_t x;
    int64_t y;
    int inf;
} Point;

static int64_t mod_inv(int64_t a, int64_t p) {
    int64_t t = 0, newt = 1;
    int64_t r = p, newr = a % p;
    while (newr != 0) {
        int64_t q = r / newr;
        int64_t tmp = newt;
        newt = t - q * newt;
        t = tmp;
        tmp = newr;
        newr = r - q * newr;
        r = tmp;
    }
    if (r > 1) return -1;
    if (t < 0) t += p;
    return t;
}

static Point point_add(Point P, Point Q) {
    if (P.inf) return Q;
    if (Q.inf) return P;
    if (P.x == Q.x && (P.y + Q.y) % P_FIELD == 0) {
        Point R = {0,0,1};
        return R;
    }
    int64_t m;
    if (P.x != Q.x || P.y != Q.y) {
        int64_t denom = (Q.x - P.x) % P_FIELD;
        if (denom < 0) denom += P_FIELD;
        m = ((Q.y - P.y) * mod_inv(denom, P_FIELD)) % P_FIELD;
    } else {
        int64_t denom = (2 * P.y) % P_FIELD;
        m = ((3 * P.x * P.x + A_COEFF) * mod_inv(denom, P_FIELD)) % P_FIELD;
    }
    if (m < 0) m += P_FIELD;
    int64_t x3 = (m * m - P.x - Q.x) % P_FIELD;
    if (x3 < 0) x3 += P_FIELD;
    int64_t y3 = (m * (P.x - x3) - P.y) % P_FIELD;
    if (y3 < 0) y3 += P_FIELD;
    Point R = {x3, y3, 0};
    return R;
}

static Point point_mul(int64_t k, Point P) {
    Point R = {0,0,1};
    while (k > 0) {
        if (k & 1) R = point_add(R, P);
        P = point_add(P, P);
        k >>= 1;
    }
    return R;
}

void dual_ec_drbg(int64_t seed, int blocks) {
    Point G = {3, 65, 0};
    Point Q = {83, 97, 0};
    int64_t s = seed;
    for (int i = 0; i < blocks; i++) {
        Point sP = point_mul(s, G);
        s = sP.x % P_FIELD;
        Point rP = point_mul(s, Q);
        printf("%ld\n", rP.x % P_FIELD);
    }
}

#ifndef NO_MAIN
int main(int argc, char **argv) {
    int64_t seed = 7;
    int blocks = 5;
    if (argc > 1) seed = atoll(argv[1]);
    if (argc > 2) blocks = atoi(argv[2]);
    dual_ec_drbg(seed, blocks);
    return 0;
}
#endif
```
</details>

<a name="cmainc"></a>
### c/main.c
<details>
<summary>Show c/main.c</summary>
```c
#include <stdio.h>
#include <string.h>
#include "ciphers.h"

int main(int argc, char **argv) {
    if (argc < 3) {
        printf("Usage: %s <cipher> <text> [key_length]\n", argv[0]);
        return 1;
    }
    const char *mode = argv[1];
    const char *text = argv[2];
    if (strcmp(mode, "caesar") == 0) {
        caesar_break(text);
    } else if (strcmp(mode, "vigenere") == 0 && argc >= 4) {
        int key_length = atoi(argv[3]);
        vigenere_break(text, key_length);
    } else {
        printf("Unsupported mode or missing arguments\n");
    }
    return 0;
}
```
</details>

<a name="codehelloasm"></a>
### code/hello.asm
<details>
<summary>Show code/hello.asm</summary>
```asm
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
```
</details>

<a name="codehelloc"></a>
### code/hello.c
<details>
<summary>Show code/hello.c</summary>
```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc > 1) {
        printf("Hello, %s!\n", argv[1]);
    } else {
        printf("Hello, world!\n");
    }
    return 0;
}
```
</details>

<a name="codehellopy"></a>
### code/hello.py
<details>
<summary>Show code/hello.py</summary>
```python
import sys

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "world"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```
</details>

<a name="papertex"></a>
### paper.tex
<details>
<summary>Show paper.tex</summary>
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\title{Your Research Title}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
A brief summary of the paper.
\end{abstract}

\section{Introduction}
Introduce the context and motivation of your research.

\section{Related Work}
Describe previously published work relevant to your paper.

\section{Methodology}
Detail your research approach and methods.

\section{Experiments}
Provide experiments, results, and analysis.

\section{Code Examples}
This appendix accompanies the repository and describes how to build and
execute the included examples written in C, Python, and x86\textendash64
assembly. Each program prints a greeting using an optional name
parameter supplied on the command line.

\subsection{C Program}
The source file \verb|code/hello.c| may be compiled using GCC as
follows:
\begin{verbatim}
gcc -o hello_c code/hello.c
\end{verbatim}
Running \verb|./hello_c| prints \texttt{``Hello, world!''}. Supplying a
name argument, e.g. \verb|./hello_c Alice|, results in the output
\texttt{``Hello, Alice!''}.

\subsection{Python Program}
The script \verb|code/hello.py| requires Python~3 and is executed with:
\begin{verbatim}
python3 code/hello.py [name]
\end{verbatim}
If a name is provided, the program prints a personalized greeting; otherwise,
it defaults to \texttt{``Hello, world!''}.

\subsection{Assembly Program}
An x86\textendash64 NASM example is provided in \verb|code/hello.asm|.
It can be assembled and linked with:
\begin{verbatim}
nasm -felf64 code/hello.asm
gcc hello.o -o hello_asm
\end{verbatim}
Executing \verb|./hello_asm Bob| prints the message
\texttt{``Hello, Bob!''}. If no parameter is supplied, the default output is
\texttt{``Hello, world!''}.

\section{Conclusion}
Summarize your findings and future work.

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```
</details>

<a name="pythonREADMEmd"></a>
### python/README.md
<details>
<summary>Show python/README.md</summary>
```markdown
# Python Cipher Analysis

This directory provides analysis tools for classic ciphers:

- **Caesar**: brute force decryption of all possible shifts.
- **Vigenere**: estimate key from frequency analysis given a key length.
- **Enigma**: simplified rotor/plugboard simulation.
- **insecure_rng**: demonstrates a Dual EC DRBG style random generator that
  is intentionally insecure. **Do not use in production!**
- **secure_rng**: example wrapper around Python's cryptographically secure
  `secrets` module.

Run `python analyze.py --help` for options.
```
</details>

<a name="pythonanalyzepy"></a>
### python/analyze.py
<details>
<summary>Show python/analyze.py</summary>
```python
import argparse
from collections import Counter

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_break(ciphertext):
    ciphertext = ciphertext.upper()
    possibilities = {}
    for shift in range(26):
        decrypted = ''.join(
            ALPHABET[(ALPHABET.index(c) - shift) % 26] if c in ALPHABET else c
            for c in ciphertext
        )
        possibilities[shift] = decrypted
    return possibilities


def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    result = []
    key_index = 0
    for c in ciphertext.upper():
        if c in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            index = (ALPHABET.index(c) - shift) % 26
            result.append(ALPHABET[index])
            key_index += 1
        else:
            result.append(c)
    return ''.join(result)


def vigenere_break(ciphertext, key_length):
    ciphertext = ''.join(c for c in ciphertext.upper() if c in ALPHABET)
    columns = ['' for _ in range(key_length)]
    for i, c in enumerate(ciphertext):
        columns[i % key_length] += c
    key = ''
    for col in columns:
        freqs = Counter(col)
        most_common = freqs.most_common(1)[0][0]
        shift = (ALPHABET.index(most_common) - ALPHABET.index('E')) % 26
        key += ALPHABET[shift]
    plaintext = vigenere_decrypt(ciphertext, key)
    return key, plaintext


# Simple Enigma simulation with 3 rotors and plugboard
def enigma_encrypt(text, rotors, reflector, plugboard):
    def apply_plugboard(c):
        return plugboard.get(c, c)

    result = []
    r_positions = [0, 0, 0]
    for ch in text.upper():
        if ch not in ALPHABET:
            result.append(ch)
            continue
        c = apply_plugboard(ch)
        for i in range(3):
            offset = (ALPHABET.index(c) + r_positions[i]) % 26
            c = rotors[i][offset]
        c = reflector[ALPHABET.index(c)]
        for i in reversed(range(3)):
            offset = rotors[i].index(c)
            c = ALPHABET[(offset - r_positions[i]) % 26]
        c = apply_plugboard(c)
        result.append(c)
        r_positions[0] = (r_positions[0] + 1) % 26
        if r_positions[0] == 0:
            r_positions[1] = (r_positions[1] + 1) % 26
            if r_positions[1] == 0:
                r_positions[2] = (r_positions[2] + 1) % 26
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(description="Cipher analysis tools")
    subparsers = parser.add_subparsers(dest="command")

    caesar_p = subparsers.add_parser("caesar_break")
    caesar_p.add_argument("ciphertext")

    vig_p = subparsers.add_parser("vigenere_break")
    vig_p.add_argument("ciphertext")
    vig_p.add_argument("key_length", type=int)

    enigma_p = subparsers.add_parser("enigma_sim")
    enigma_p.add_argument("text")

    args = parser.parse_args()

    if args.command == "caesar_break":
        possibilities = caesar_break(args.ciphertext)
        for shift, text in possibilities.items():
            print(f"Shift {shift}: {text}")
    elif args.command == "vigenere_break":
        key, text = vigenere_break(args.ciphertext, args.key_length)
        print("Estimated key:", key)
        print("Plaintext:", text)
    elif args.command == "enigma_sim":
        rotors = [
            'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        ]
        reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        plugboard = {}
        text = enigma_encrypt(args.text, rotors, reflector, plugboard)
        print(text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```
</details>

<a name="pythondual_ec_drbgpy"></a>
### python/dual_ec_drbg.py
<details>
<summary>Show python/dual_ec_drbg.py</summary>
```python
P = (3, 65)
Q = (83, 97)
p = 233
A = 1

# Elliptic curve utilities over F_p

def inv_mod(a, p):
    """Return modular inverse of a mod p."""
    return pow(a, -1, p)

def add(Pt, Qt):
    if Pt is None:
        return Qt
    if Qt is None:
        return Pt
    x1, y1 = Pt
    x2, y2 = Qt
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if Pt != Qt:
        m = ((y2 - y1) * inv_mod((x2 - x1) % p, p)) % p
    else:
        m = ((3 * x1 * x1 + A) * inv_mod((2 * y1) % p, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3

def mul(k, Pt):
    result = None
    addend = Pt
    while k:
        if k & 1:
            result = add(result, addend)
        addend = add(addend, addend)
        k >>= 1
    return result

def dual_ec_drbg(seed, blocks=5):
    s = seed
    out = []
    for _ in range(blocks):
        s = mul(s, P)[0]
        r = mul(s, Q)[0]
        out.append(r)
    return out

if __name__ == "__main__":
    from sys import argv
    seed = int(argv[1]) if len(argv) > 1 else 7
    blocks = int(argv[2]) if len(argv) > 2 else 5
    print(dual_ec_drbg(seed, blocks))
```
</details>

<a name="pythoninsecure_rngpy"></a>
### python/insecure_rng.py
<details>
<summary>Show python/insecure_rng.py</summary>
```python
"""Dual EC DRBG style insecure random number generator.

WARNING: This implementation is intentionally insecure and provided
only for demonstration purposes. Do NOT use for real cryptographic
applications or in production systems.
"""

import os

# These constants are taken from the NIST P-256 curve but the output
# generation is intentionally flawed and predictable.
P = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
Q = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
G = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162cb13b12a14cdbdb1cb4c20ad0c6f1e2

class DualECDRBG:
    """Very simplified and insecure Dual_EC_DRBG-like generator."""

    def __init__(self, seed: int | None = None) -> None:
        if seed is None:
            seed = int.from_bytes(os.urandom(32), "big")
        self.state = seed % P

    def next_bytes(self, nbytes: int = 32) -> bytes:
        # The real algorithm uses elliptic curve point multiplication.
        # Here we use a trivial modular squaring step followed by a
        # predictable linear transformation, which is insecure.
        self.state = pow(self.state, 2, P)
        r = (self.state * Q) % P
        out = (r * G) % P
        return out.to_bytes(64, "big")[:nbytes]


def demo() -> None:
    rng = DualECDRBG()
    for _ in range(5):
        print(rng.next_bytes(16).hex())


if __name__ == "__main__":
    demo()
```
</details>

<a name="pythonsecure_rngpy"></a>
### python/secure_rng.py
<details>
<summary>Show python/secure_rng.py</summary>
```python
"""Secure random number generator wrapper using Python's secrets module."""

import secrets

class SecureRNG:
    """Provides cryptographically strong random bytes."""

    def next_bytes(self, nbytes: int = 32) -> bytes:
        return secrets.token_bytes(nbytes)


def demo() -> None:
    rng = SecureRNG()
    for _ in range(5):
        print(rng.next_bytes(16).hex())


if __name__ == "__main__":
    demo()
```
</details>

<a name="referencesbib"></a>
### references.bib
<details>
<summary>Show references.bib</summary>
```bibtex
@article{example,
  title={Example reference},
  author={Doe, Jane},
  journal={Journal of Examples},
  year={2024}
}
```
</details>

---
### Legend
* This document includes all source files.
* Hover over the Table of Contents links to jump to sections.
* Code blocks are syntax highlighted.

### Index
1. Source code
2. Assembly examples
3. Bash scripts
4. Research paper template

---

_This archive is AI-assisted and provided solely for research and educational purposes._

