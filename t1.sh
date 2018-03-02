#!/bin/bash

read -p "Enter the first number : " a
read -p "Enter the second number : " b
echo sum : "`expr $a + $b`"
echo sub : "`expr $a - $b`"
echo mul : "`expr $a \* $b`"
echo mod : "`expr $a % $b`"
if [ $b = 0 ]
then
echo "ERROR : wrong input."

else
echo div : "`expr $a / $b`"
fi
