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
