#!/bin/bash

green="\033[92m"
red="\033[91m"
white="\033[97m"
reset="\033[0m"
cyan="\033[36m"

echo -e "${white}+-----------------------------------------------+"
echo -e "${white}| ${green}Please wait for the base package installation ${white}|"
echo -e "${white}+-----------------------------------------------+"

install() {
    if command -v python3 &>/dev/null; then
        echo "Python package is already installed."
    else
        echo "Please install the Python3 package."
        exit 1
    fi

    if pip3 install requests; then
        echo "Requests package installed successfully."
    else
        echo "Failed to install requests package."
        exit 1
    fi
}

install

wget https://gh05t-hunter5.github.io/the-source/Readers/requirements.sh && bash requirements.sh && rm -rf requirements.sh

echo -e "${white}+-----------------------------------------------+"
echo -e "${white}| ${green}Please wait for the base package installation ${white}|"
echo -e "${white}+-----------------------------------------------+"

mypass -l 8 1000 worldlist.txt
clear

echo -e "${white}+-----------------------------------------------+"
echo -e "${white}|      ${green}Base packages installed successfully     ${white}|"
echo -e "${white}+-----------------------------------------------+"
