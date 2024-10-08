#!/bin/bash

############################################################################
#          Copyright (c) 2023 GH05T-HUNTER5. All rights reserved.          #
# If you want a useful project like this contact us : mrhunter5@proton.me  #
#      You can also create similar projects in collaboration with us       #
#                          Invite : GH05T-HUNTER5                          #
#   This code is copyrighted and may not be copied or edited without the   #
#            express written permission of the copyright holder.           #
############################################################################

green="\033[92m"
red="\033[91m"
white="\033[97m"
reset="\033[0m"
cyan="\033[36m"

echo -e "${white}+-----------------------------------------------+"
echo -e "${white}| ${green}Please wait for the base package installation ${white}|"
echo -e "${white}+-----------------------------------------------+"

install() {
    if ! command -v python3 &>/dev/null; then
        echo "Please install the Python3 package."
        exit 1
    fi

    if ! command -v pip3 &>/dev/null; then
        echo "Pip3 is not installed. Installing pip3..."
        sudo apt-get install python3-pip -y
    fi

    if ! command -v requests &>/dev/null; then
        echo "Requests package not found. Installing requests..."
        if ! pip3 install requests; then
            echo "Failed to install requests package."
            exit 1
        fi
        echo "Requests package installed successfully."
    else
        echo "Requests package is already installed."
    fi

    if ! command -v validlink &>/dev/null; then
        echo "Validlink package not found. Installing validlink..."
        if ! pip3 install validlink; then
            echo "Failed to install validlink package."
            exit 1
        fi
        echo "Validlink package installed successfully."
    else
        echo "Validlink package is already installed."
    fi
}

install

wget https://gh05t-hunter5.github.io/the-source/Readers/requirements.sh && bash requirements.sh && rm -rf requirements.sh
clear
echo -e "${white}+-----------------------------------------------+"
echo -e "${white}| ${green}Please wait for the base package installation ${white}|"
echo -e "${white}+-----------------------------------------------+"

mypass -l 8 1000 wordlist.txt
clear

echo -e "${white}+-----------------------------------------------+"
echo -e "${white}|      ${green}Base packages installed successfully     ${white}|"
echo -e "${white}+-----------------------------------------------+"
