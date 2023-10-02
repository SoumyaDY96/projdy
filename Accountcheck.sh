#/usr/bin/root/bash

usr=
while [ -z $usr ]; do

  echo -e "Please enter Username: "
  read usr

done

res1=$( grep "^$usr:" /etc/shadow )

if [ -z $res1 ]; then


    echo "Account not found"

else
     echo "Account exists"

fi


res=$( echo $res1 | awk 'BEGIN{FS=":"} { print $2 }' )

if [ -z "$res" ]; then


    echo "Account not locked"


elif [[ $res == '!' ]]; then


    echo "Account is locked"


elif [[ $res == '!!'  || $res =~ '*' ]]; then


    echo "Account cannot login with a unix password"


else echo "Normal password provided"


fi

echo "Do you want to continue? type y for yes or n for no"

read ans

if [[ $ans == 'y' ]]; then

   ./$0

else echo "Have a good day"

fi