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
