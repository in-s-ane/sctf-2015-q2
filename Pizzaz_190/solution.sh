#!/bin/bash

enc="221.164.100.10.237.97.167.177.205.54.30.53.124.232.78.134.215.10.37.45.30.244.131.235.116.131.237.237.85.27.210.205.35.76.5.5.210.102.157.157.3.96.114.25.91.238.192."

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-{} "
flag=""

# the flag is 47 characters long
for i in $(seq 1 47); do
    for (( j=0; j<${#alphabet}; j++ )); do
        char=${alphabet:$j:1}
        candidate=$flag$char
        output=$(./pizazz $candidate)
        # The encrypted flag begins with our output!
        if [[ "$enc" == "$output"* ]]; then
            flag+=$char
            echo $flag
            break
        fi
    done
done
echo $flag

# flag{Z-0rder_curv3s_and_janky_p3rmutat10ns_FTW}
