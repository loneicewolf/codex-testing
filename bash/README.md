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

Source the file in your shell to make the functions available:

```bash
source aliases.sh
```
