#!/bin/sh
echo "Enter a number: "
read n
temp=$n
re=0
while [ $n != 0 ]
do
    r=$(( $n % 10 ))
    re=$(( $re * 10 + $r ))
    n=$(( $n / 10 ))
done
if [ $re -eq $temp ]
then
    echo "The given number is a Palindrome"
else
    echo "The given number is not a Palindrome"
fi
