#!/bin/bash

file=mem.txt

function applymask () {
  m=$2
  local v=$(printf "%036s" $( echo "2o $1 p" | dc ))
  x=0
  for (( i=0; i < ${#m}; i++ )); do
    if [ ${m:$i:1} != "0" ]; then
      v=${v:0:$i}${m:$i:1}${v:$(( i+1 ))}
    fi
  done
  echo "$v"
}

function permutex () {
  v=$1
  x=0
  for (( i=0; i < ${#v}; i++ )); do
    if [ ${v:$i:1} == "X" ]; then
      let x++
    fi
  done
  xs=()
  if [ $x -gt 0 ]; then
    for (( i=0; i < 2 ** x; i++ )); do
      t=$(printf "%0${x}s" $( echo "2o $i p" | dc ))
      xs=( ${xs[*]} "$t" )
    done
  fi
  for xt in ${xs[*]}; do
    vt=$v
    x=0
    for (( i=0; i < ${#v}; i++ )); do
      if [ ${v:$i:1} == "X" ]; then
        vt=${vt:0:$i}${xt:$x:1}${vt:$(( i+1 ))}
        let x++
      fi
    done
    echo "2i $vt p" | dc
  done
}

declare -a memory=()
while read l; do
  echo -n "."
  c=$(echo $l | cut -d= -f1 | sed "s/ //g")
  p=$(echo $l | cut -d= -f2 | sed "s/ //g")
  if [ "a$c" == "amask" ]; then
    mask=$p
  else
    addr=$( echo "${c:4}" | sed -E "s/\]//" )
    
    addrn=$(applymask $addr $mask)
    for a in $(permutex $addrn); do
      val=$p
      memory[$a]=$val
    done
  fi
done < $file
echo 

s=0
for v in ${memory[@]}; do
  s=$(( s + v ))
done
echo "sum: $s"
