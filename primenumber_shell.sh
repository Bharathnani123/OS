#!/bin/sh
echo "Enter a number: "
read n
flag=0
if [ $n -le 1 ]
then
    flag=1
else
    i=2
    a=$(( $n / 2 ))
    while [ $i -le $a ]
    do
        rem=$(( $n % $i ))
        if [ $rem -eq 0 ]
        then
            flag=1;
            break;
        fi
        i=$(( $i + 1 ))
    done
fi
if [ $flag -eq 0 ]
then
    echo "$n is a prime number"
else
    echo "$n is not a prime number."
fi
