#!/bin/bash
if [[ $# == 0 ]]
then
echo "Enter subdomain file "
else
for i in $(cat $1)
do

i=$(echo $i | cut -d "/" -f 3)

curl --expect100-timeout 5 -s "https://$i" -H "Origin: https://www.evil.com" -I >  c
curl --expect100-timeout 5 -s "http://$i" -H "Origin: https://www.evil.com" -I > c2






if [[ $(cat c |grep -i "access-control-allow-credentials: true") ]]
then
	if [[ $(cat c | grep -i "access-control-allow-origin: " ) ]]
	then
		echo -e "$i \e[5m------>>>> \e[25m \e[92mVuln  \e[92m "
		cat c |grep  -i --color "access-control-allow-credentials: true" && cat c | grep -i --color "access-control-allow-origin: "
	fi


elif [[ $(cat c2 |grep -i "access-control-allow-credentials: true") ]]
then
	if [[ $(cat c2 | grep -i "access-control-allow-origin: " ) ]]
	then
		echo -e "$i \e[5m------>>>> \e[25m \e[92mVuln  \e[92m "
		cat c2 |grep -i --color "access-control-allow-credentials: true" && cat c2 | grep -i --color "access-control-allow-origin: "
	fi



else
echo -e "\e[39m $i"

fi
done
fi
rm c
rm c2
echo " Done as u can see :) hope u find something "