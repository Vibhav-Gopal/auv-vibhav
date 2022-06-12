#!/bin/bash
echo "Enter the name of the file along with the extension to search for"
read filename
if [ -e $filename ]
then
    WD=`pwd`

    echo $WD/$filename is the path

else
    echo "The file doesn't exist in the current working directory"
fi

[ -w $filename ] && echo "You have permission to edit the file:- $filename" || echo "You do NOT have permission to edit the file:- $filename"


