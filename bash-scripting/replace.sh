#!/bin/bash
file="hexa.txt"
old="0xA0"
new="0x50"

echo -e "\nFile" $file "before replacement\n\n" 
echo -e '\n... Opening' $file ' ...\n\n'
cat $file
echo -e '\n'

read -p "Are you sure you want to replace ? ? (y/n) : " yn 
if [[ $yn == 'y' || $yn == 'Y' ]]; then
    sed -i "s|$old|$new|g" $file
    old="0xFF"
    new="0x7F"
    sed -i "s|$old|$new|g" $file

else
    echo -e '\nInvalid Input\n'
    echo -e '\nNo changes applied\n'
fi
echo -e '\n... Opening' $file ' ...\n\n'
cat $file
echo -e '\n'
