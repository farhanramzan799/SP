#!/bin/bash

arr=(`ls -l $1`)
arr1=(`ls -l $3`)
echo ${arr[*]}
echo $0
echo ${arr1[*]}
if [ $# = 2 ]
then
	if [ ${arr[3]} = $2 ]
	then
	echo "onwer : " ${arr[2]}
	echo "group : " ${arr[3]}
	echo "permission : " ${arr[0]}
	echo "filename : " ${arr[8]}
	echo "cheating : "0
	fi
else
	if [ $# = 4 ]
	then
		if [ ${arr[3]} = $2 ] && [ ${arr1[3]} = $4 ]
		then
		arr2=(`diff file.txt file1.txt`)
		if [ ${arr2[*]} =  ]
		then
		echo "cheating : 1"
else
		echo "onwer : " ${arr[2]}
	echo "group : " ${arr[3]}
	echo "permission : " ${arr[0]}
	echo "filename : " ${arr[8]}
	echo "cheating : "0
	echo ""
	echo "onwer : " ${arr1[2]}
	echo "group : " ${arr1[3]}
	echo "permission : " ${arr1[0]}
	echo "filename : " ${arr1[8]}
	echo "cheating : "0
	
		fi
		fi

	fi

fi


