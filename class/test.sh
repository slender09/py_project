#!/usr/bin/bash

echo "script name is $0"

echo "all argvs $*, num $#"

j=1
for i in $*
do
    echo "the $j argv is $i"
    let j++
done
