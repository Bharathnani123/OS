#!/bin/sh
echo "Enter two numbers: "
read a
read b
echo "Operations to be Performed: "
echo "1. Add"
echo "2. Sub"
echo "3. Multiply"
echo "4. Division"
echo "Enter your Choice: "
read c
while [ $c -le 4 ]
do
    case "$c" in
        "1") sum=$(( $a + $b ))
            echo "$a + $b = $sum"
        ;;
        "2") diff=$(( $a - $b ))
            echo "$a - $b = $diff"
        ;;
        "3") mul=$(( $a * $b))
            echo "$a * $b = $mul"
        ;;
        "4") div=$(( $a / $b ))
            echo "$a / $b = $div"
        ;;
        esac
    echo "Enter your choice: "
    read c
done
