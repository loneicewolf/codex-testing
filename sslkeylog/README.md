# SSLKEYLOGFILE Helper Scripts

This folder contains small scripts to set the `SSLKEYLOGFILE` environment
variable on Linux and Windows. The variable instructs compatible applications
(e.g. browsers or command line tools using OpenSSL) to log TLS session keys to a
file so the traffic can be decrypted in debugging tools like Wireshark.

## Linux

Source the script to set the variable for your shell:

```bash
source ./linux/set_sslkeylog.sh
```

Optionally provide a path to the log file:

```bash
source ./linux/set_sslkeylog.sh /tmp/mykeys.log
```

## Windows

Run the PowerShell script in your session:

```powershell
.\windows\set_sslkeylog.ps1
```

Provide a custom file path if desired:

```powershell
.\windows\set_sslkeylog.ps1 -LogFile C:\\temp\\keys.log
```
