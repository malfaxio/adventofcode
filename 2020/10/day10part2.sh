#!/bin/bash

i=0
d1=0
d3=0
a=( 0 )
while read j; do
  a=(${a[*]} $j)
  if [ $i -gt 0 ]; then
    d=$(( $j - $oj ))
    if [ $d -eq 1 ]; then
      let d1++
    elif [ $d -eq 3 ]; then
      let d3++
    fi
  fi
  oj=$j
  let i++
done <<< "$( cat jt.txt | sort -n )"

a=( ${a[*]} $(( ${a[${#a[@]} - 1]} + 3 )) )
echo ${a[*]}

dropable=0
for j in $(seq 1 $(( i - 1 )) )
do
  t1=${a[j-1]}
  t2=${a[j+1]}
  r=$(( t2-t1 ))
  if [ $r -le 3 ]; then
    let dropable++
    echo ${a[j]} drop
  fi
done

s=2
for y in $(seq 1 $(( dropable - 1 )) )
do
  t=$(( 2 ** y ))
  let s=s+t
done
echo $s
