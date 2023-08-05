#!/bin/bash
# Copyright (c) 2023 GH05T-HUNTER5. All rights reserved.
green=$'\e[1;32m'
clear
echo -e "${green}
 ██████╗ ██╗██████╗ ██████╗ ██╗     ██╗████████╗███████╗
 ██╔══██╗██║██╔══██╗██╔══██╗██║     ██║╚══██╔══╝╚══███╔╝
 ██║  ██║██║██████╔╝██████╔╝██║     ██║   ██║     ███╔╝
 ██║  ██║██║██╔══██╗██╔══██╗██║     ██║   ██║    ███╔╝
 ██████╔╝██║██║  ██║██████╔╝███████╗██║   ██║   ███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝ 
"
sleep 2
install() {
	if [[ $(command -v python3) ]]; then
		echo "Python package installed successfully"
	else
		echo "Please install the Python3 package"
		exit
	fi
	pip install requests
}

install
clear
