Here's a shell script to reverse a number:

#!/bin/bash

# Read the number from the user
echo -n "Enter a number: "
read num

# Initialize variables
rev=0
temp=$num

# Reverse the number
while [ $temp -gt 0 ]
do
    # Get the last digit
    digit=$((temp % 10))
    
    # Append the digit to rev
    rev=$((rev * 10 + digit))
    
    # Remove the last digit from temp
    temp=$((temp / 10))
done

# Display the reversed number
echo "Reversed number is: $rev"



