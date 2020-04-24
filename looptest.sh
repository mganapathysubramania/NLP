#!/bin/bash

# Replace this line with one or more shell commands
# You may write to intermediate text files on disk if necessary
#cat -
	#for i in "${splitlines[@]}"; do
	#echo $i
#done

declare -i count=0
# while read line; do  
for line in $(cat test.in.txt)
do
    IFS="," 
	read -ra splitlines <<< "$line"
	IFS=" "
	read -ra stringthree <<< "${splitlines[2]}"
	
	#if [ `echo ${splitlines[4]} | grep -c ${stringthree[0]} ` -gt 0 ]
	#then
	#	echo 1
	#fi
	
	IFS=" "
	read -ra stringfive <<< "${splitlines[4]}"
	value1=${stringthree[0]}
	for i in "${stringfive[@]}"
	do
	if test "$i" == "$value1"
	then
		let "count++"
		#ct= $ (( $ct+1 ))
	fi
done	
	
done #< test.in.txt   
echo $count

cmd /k