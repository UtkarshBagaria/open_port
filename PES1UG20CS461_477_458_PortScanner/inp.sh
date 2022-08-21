#!/bin/bash

args=("$@")

if [ "${args[0]}" == "-ps" ] || [ "${args[0]}" == "--port-scan" ]
then
	sudo python3 "/home/utkarsh/Desktop/Industry Problem/mainx.py" ${args[1]} ${args[2]} 
elif [ "${args[0]}" == "-bg" ] || [ "${args[0]}" == "--banner-grab" ]
then
	curl -I ${args[1]}
elif [ "${args[0]}" == "-a" ] || [ "${args[0]}" == "--all" ]
then
    sudo python3 "/home/utkarsh/Desktop/Industry Problem/mainx.py" ${args[1]} ${args[2]} 
	curl -I ${args[1]}
fi

