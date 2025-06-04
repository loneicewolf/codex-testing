#!/bin/bash
# Pure bash Dual_EC_DRBG demo with small curve
p=233
A=1
Px=3
Py=65
Qx=83
Qy=97
seed=${1:-7}
blocks=${2:-5}

inv_mod() {
  local a=$1
  local p=$2
  for ((i=1;i<p;i++)); do
    if (( (a*i) % p == 1 )); then
      echo $i
      return
    fi
  done
}

add_point() {
  local x1=$1 y1=$2 x2=$3 y2=$4
  if (( x1 == -1 )); then echo "$x2 $y2"; return; fi
  if (( x2 == -1 )); then echo "$x1 $y1"; return; fi
  if (( x1==x2 && (y1 + y2) % p == 0 )); then
    echo "-1 0"
    return
  fi
  local m
  if (( x1==x2 && y1==y2 )); then
    local denom=$(( (2*y1) % p ))
    local inv=$(inv_mod $denom $p)
    m=$(( (3*x1*x1 + A)*inv % p ))
  else
    local denom=$(( (x2 - x1 + p) % p ))
    local inv=$(inv_mod $denom $p)
    m=$(( ( (y2 - y1 + p) % p ) * inv % p ))
  fi
  local x3=$(( (m*m - x1 - x2) % p ))
  if (( x3 < 0 )); then x3=$((x3+p)); fi
  local y3=$(( (m*(x1 - x3) - y1) % p ))
  if (( y3 < 0 )); then y3=$((y3+p)); fi
  echo "$x3 $y3"
}

mul_point() {
  local k=$1 x=$2 y=$3
  local hx=-1 hy=0
  while (( k>0 )); do
    if (( k & 1 )); then
      read hx hy <<<$(add_point $hx $hy $x $y)
    fi
    read x y <<<$(add_point $x $y $x $y)
    k=$((k>>1))
  done
  echo "$hx $hy"
}

for ((i=0;i<blocks;i++)); do
  read sx sy <<<$(mul_point $seed $Px $Py)
  seed=$sx
  read rx ry <<<$(mul_point $seed $Qx $Qy)
  echo $rx
  seed=$sx
done
