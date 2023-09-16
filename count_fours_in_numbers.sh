#!/bin/bash
#Count 4 in numbers
read -r -p "Provide a number: " ans

cnt=0
for ((i=4; i<=ans; i++))
do
  j=$i
  while [ $j -gt 0 ]
  do
    if [ $((j%10)) -eq 4 ]
    then
      cnt=$((cnt+1))
      break
    fi
    j=$((j/10))
  done
done

echo $cnt