#!/bin/bash
a=true


while $a; do

echo "Please enter Username"


read usr

res1=$( grep "^$usr:" /etc/shadow )



if [ -z $res1 ]; then
   
   
    echo "Account not found"
 
    :

else

   
     echo "Account exists"

   
     res=$( echo $res1 | awk 'BEGIN{FS=":"} { print $2 }' )

     if [[ -z "$res" ]]; then


        echo "Account not locked"
 
        :


     elif [[ $res == '!' ]]; then

 
       echo "Account is locked."

        :

    
 elif [[ $res == '!!'  || $res =~ '*' ]]; then

 
       echo "Account cannot login with a unix password."

        :


     else echo "Normal password provided."

            :     
     fi

fi
    
echo "Do you want to continue? type y for yes or n for no"

read ans

if [[ $ans == 'y' ]]; then

    continue

else echo "Have a good day"; break

fi

done