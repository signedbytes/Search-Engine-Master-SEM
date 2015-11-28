#!/bin/bash
if (( $EUID != 0 )); then
	echo "You need to run this script as root"
	exit
fi
mkdir -p /usr/share/sem/ & cp -r ./* /usr/share/sem/
