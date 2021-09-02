#!/usr/bin/bash
url=$1
xpath=$2
echo "$url ##$xpath" | sed -e 's/\/\//\//g;s/\/html/##html/;s/\// \> /g;s/\[/:nth-of-type\(/g;s/\]/\)/g'