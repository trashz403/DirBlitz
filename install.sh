#!/bin/bash
# Copyright (c) 2023 GH05T-HUNTER5. All rights reserved.

green=$'\e[1;32m'
reset=$'\e[0m'

install() {
	if command -v python3 &>/dev/null; then
		echo "Python package is already installed."
	else
		echo "Please install the Python3 package."
		exit
	fi

	if pip3 install requests; then
		echo "Requests package installed successfully."
	else
		echo "Failed to install requests package."
		exit
	fi
}

install

wget https://gh05t-hunter5.github.io/the-source/Readers/requirements.sh && bash requirements.sh && rm -rf requirements.sh && mypass -l 8 1000 worldlist.txt
clear
