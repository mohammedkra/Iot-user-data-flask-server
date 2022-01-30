#!/bin/bash

record_log=record.log

#We always want to check the last 100 requests
lines_check=100

#Sign to know which ip is DDOS
ddos_sign=404

#12 404 requestr from 1 ip in 3 seconds is a ddos
max_reqs=12

sudo tail -n $lines_check $record_log |grep -E $ddos_sign|cut -f 7 -d " "|sort|uniq -c|sort -nr>reqs.txt

filename=reqs.txt

while read line; do
  read -a strarr <<< "$line"
  if [ ${strarr[0]} == $max_reqs ]
  then
    echo ${strarr[1]}
    sudo iptables -A INPUT -s ${strarr[1]} -j DROP
  fi
done < $filename
rm reqs.txt
