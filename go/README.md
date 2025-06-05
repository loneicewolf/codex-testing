# Go GUI Cipher Helper

This directory contains a Go rewrite of the Python GUI for breaking
Caesar ciphers and decrypting Vigenère text. The program uses the
[Fyne](https://fyne.io/) toolkit to create the interface.

## Building

```
cd go
go build
```

Make sure you have Go installed and can fetch modules from the internet.
If module download fails in your environment, you may need to adjust the
go proxy or provide the dependencies manually.
```
