#!/bin/bash

for file in /home/Administrator/Desktop/Documents/together/*
do
if [ -d "$file" ]
then 
  echo "$file is directory"
  cd "$file"
  grep DFT energy gap: *.outmol | tail -1 >> /home/Administrator/Desktop/Documents/together/Eg.csv
  grep valence band edge: *.outmol | tail -1 >> /home/Administrator/Desktop/Documents/together/VBM.csv
  grep conduction band edge: *.outmol | tail -1 >> /home/Administrator/Desktop/Documents/together/CBM.csv
elif [ -f "$file" ]
then
  echo "$file is file"
fi
done







####!/bin/bash

#T_HOME=/home/Administrator/Desktop/Documents/1-20

#pushd $T_HOME
#OUTPUTFILE='ls | grep "GeomOpt$"'
#echo $OUTPUTFILE
#popd

#for entry in $OUTPUTFILE
#do
 #   echo path is : $T_HOME/$entry
 #    ls -l $T_HOME/$entry | sed '1d' | awk -v entry="$entry" '{printf("%-10d, %-50s, %-10s \n", $5, $9, entry)}' > /home/Administrator/Desktop/Documents/1-20/$entry.txt
 #done
 ###

