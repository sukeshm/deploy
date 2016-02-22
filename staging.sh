#!/bin/sh
cd /C/Users/Sukesh/Documents/GitHub/<Repository>
git fetch --prune
git checkout origin/master
git branch -D staging
git checkout -b staging
echo -------------------------------
for service in C:\buildStaging.py
do
echo Merging $service
git merge --no-ff origin/$service | grep 'failed' &> /dev/null 
if [ $? == 0 ]; then
   git merge --abort
   echo "MERGE IS ABORTED FOR THE CARD" $service  
else
	echo Merge is done
fi

echo ------------------------------------
sleep 1
done
git push origin staging -f