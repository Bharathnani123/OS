#!/bin/sh
echo "Enter a number: "
read n
res=0
num=0
temp=$n
while [ $temp -ne 0 ]
do
    num=$(( $num + 1 ))
    temp=$(( $temp / 10 ))
done
temp=$n
while [ $temp -ne 0 ]
do
    r=$(( $temp % 10 ))
    re=1
    i=1
    while [ $i -le $num ]
    do
        re=$(( $re * $r ))
        i=$(( $i + 1 ))
    done
    res=$(( $res + $re ))
    temp=$(( $temp / 10 ))
done
if [ $res -eq $n ]
then
    echo "$n is an Armstrong number"
else
    echo "$n is not an Armstrong number"
fi
