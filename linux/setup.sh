#!/bin/bash
if (( $EUID != 0 )); then
	echo "You need to run this script as root"
	exit
fi
mv sem.sh /usr/bin/sem
chmod 755 /usr/bin/sem
mkdir -p /usr/share/sem/ & cp -r ./* /usr/share/sem/
