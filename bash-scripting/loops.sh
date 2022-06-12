
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

a=0

read -p "Upto what number to print " num

until [ ! $a -lt $num ]
do
   echo $a
   a=`expr $a + 1`
done

a=0

while [  "$a" -lt "$num" ]
do
   echo $a
   a=`expr $a + 1`
done


select DRINK in tea cofee water juice appe all none
do
   case $DRINK in
      tea|cofee|water|all) 
         echo "Go to canteen"
         ;;
      juice|appe)
         echo "Available at home"
      ;;
      none) 
         break 
      ;;
      *) echo "ERROR: Invalid selection" 
      ;;
   esac
done