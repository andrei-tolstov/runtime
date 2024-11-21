IFS=(
10.85.4.21
10.85.4.22
10.96.25.11
10.96.25.12
10.95.25.141
10.95.25.142
)

for line in ${IFS[@]} ; do

  echo $line
  nc -zvw1 $line 80
  nc -zvw1 $line 443
  nc -zvw1 $line 636
  nc -zvw1 $line 389
  nc -zvw1 $line 464
  nc -zvw1 $line 88
  nc -zvw1 $line 53

done
