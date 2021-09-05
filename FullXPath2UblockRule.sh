#!/usr/bin/bash
url=$1
xpath=$2

if [[ -n "$url" &&  -n "$xpath" ]]
then
        echo "$url$xpath" | sed -e 's/\/\//\//g;s/\/html/##html/;s/\// \> /g;s/\[/:nth-of-type\(/g;s/\]/\)/g'
else
        echo "Usage: $0 <url> <full xpath>"
fi
