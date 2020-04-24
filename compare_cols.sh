#!/bin/bash

declare -i count=0
 while read line; do  
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
	value1=${stringthree[0]} #value of 3 column first row
	for i in "${stringfive[@]}"
	do
	if test "$i" == "$value1"   #compare first row of third colum and looped values of 5th coulmn
	then
		let "count++"
		break #exit for loop when finds one matching value 
	fi
done	
	
done < test.in.txt   #file name
echo $count
