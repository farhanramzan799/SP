#!/bin/bash

a=(`cat file.txt`)

echo ${a[*]}
echo ${#a[*]}
echo ${#a[3]}
