#!/bin/bash

for webservmethod in GET POST PUT TRACE CONNECT OPTIONS PROPFIND DELETE PATCH;

do
printf "$webservmethod " ;
printf "$webservmethod $2 HTTP/1.1\nHost: $1\n\n" | nc $1 80 -q 3 | grep "HTTP/1.1"
printf "\n"

done
