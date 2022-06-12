#!/bin/sh
a=0
read -p "Enter the size of the number pyramid " size
while [ "$a" -lt "$size" ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done

echo "The files ending with the extension .sh are "
for FILE in ./*.sh
do
   echo $FILE
done