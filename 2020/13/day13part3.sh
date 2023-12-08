#!/bin/bash

# chinese remainder theory

file=bus.txt

bus=( `tail -1 $file | tr "," " "` )

declare -a offset=()
declare -a busid=()

i=0
for b in ${bus[@]}; do
  if [ a"$b" != "ax" ]; then
    busid=( ${busid[@]} $b )
    offset=( ${offset[@]} $i )
  fi
  let i++
done
echo ${busid[@]}
echo ${offset[@]}

b1=${busid[0]}
bu=${busid[${#busid[@]}-1]}
ou=${offset[${#busid[@]}-1]}

echo $b1 $bu $ou

t=100000345900000
c=0
bl=$(( ${#busid[@]} - 1 ))
while [ $c -lt $bl ]; do
  let t=t+b1
  let z=t%100000
  if [ $z -eq 0 ]; then
    echo $t
  fi

  for (( i=1; i < ${#busid[@]}; i++ )); do
    bid=${busid[$i]}
    off=${offset[$i]}
    t1=$(( t + off ))
    let rt=t1%bid
    if [ $rt -ne 0 ]; then
      c=0
      break
    else
      let c++
    fi
  done

done
echo $t
