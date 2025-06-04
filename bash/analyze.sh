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

