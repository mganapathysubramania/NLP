#!/bin/bash

# Replace this line with one or more shell commands
# You may write to intermediate text files on disk if necessary
	for i in $(ls test_*.txt)       #loop all file in directory
	do 
	valuethe=$(grep -c -w "the" $i) #finding value of lines that contain the 
	valuea=$(grep -c -w "a" $i)		#finding value of lines that contain a
	valuean=$(grep -c -w "an" $i)	#finding value of lines that contain an
	echo $i,$valuethe,$valuea,$valuean #printing all values
	done
	