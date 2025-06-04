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
