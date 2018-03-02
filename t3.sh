#!/bin/bash

UNIX=(Debian Redhat Ubuntu Suse Fedora)
echo ${UNIX[*]}
echo ${#UNIX[*]}
echo ${#UNIX[2]}
echo ${UNIX[*]:3:4}
UNIX=(${UNIX[*]/Ubuntu/SCOubuntu})
echo ${UNIX[*]}
UNIX=(${UNIX[*]} AIX HP-UX)
echo ${UNIX[*]}
unset UNIX[3]
linux=(${UNIX[*]})
echo ${linux[*]}
bash=(${UNIX[*]} ${linux[*]})
echo ${bash[*]}
unset linux
unset UNIX
