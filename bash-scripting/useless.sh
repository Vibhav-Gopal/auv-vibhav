#!/bin/bash
echo "Before making the folder"
ls
mkdir useless
echo 
echo "After making the folder"
ls
echo 
cd useless
touch useless.file
chmod 777 useless.file
echo "After making the file"
ls -l
echo 
cd ..

rm useless -r
echo "After removing the folder recursively"
ls