#!/bin/bash

cat | tr " " "\n" | sed '/^$/d' | sort | uniq #cat is used to read text files from input #sed is stream editor using regex we have deleted the white line#sort is used for sorting # uniq is used to get unique values
#cat | tr -s " " "\n" | sort | uniq  #cat is used to read text files from input #tr -s : replaces repeated characters listed in the set1 with single occurrence #sort is used for sorting # uniq is used to get unique values
