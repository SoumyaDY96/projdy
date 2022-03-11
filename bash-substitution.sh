#!/bin/bash


echo -e "\nThis is the first block\n\n"


I="welcome!to!JDoodle!"

del="!"

while [[ $I ]]; do

  echo "${I%"$del"*}"

  I="${I#*"$del"}"

done


: '

second one

'


echo -e "\nThis is the second block\n\n"


I="welcome!to!JDoodle!"

del="!"

while [[ $I ]]; do

echo "${I%%"$del"*}"

I="${I#*"$del"}"

done


: '


third one


'


echo -e "\nThis is the third block\n\n"


I="welcome!to!JDoodle!"

del="!"

while [[ $I ]]; do

echo "${I%%"$del"*}"

I="${I##*"$del"}"

done