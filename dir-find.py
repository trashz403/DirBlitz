#!/usr/bin/env python3

############################################################################
#          Copyright (c) 2023 GH05T-HUNTER5. All rights reserved.          #
# If you want a useful project like this contact us : mrhunter5@proton.me  #
#      You can also create similar projects in collaboration with us       #
#                          Invite : GH05T-HUNTER5                          #
#   This code is copyrighted and may not be copied or edited without the   #
#            express written permission of the copyright holder.           #
############################################################################


import sys
import requests
import signal
from urllib.parse import urljoin

green = "\033[92m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"
cyan = "\033[36m"

def print_banner():
    banner = f"""
 {white}+---------------------------------------------------------+
 {white}|{green} ██████╗ ██╗██████╗ ██████╗ ██╗     ██╗████████╗███████╗{white} |
 {white}|{green} ██╔══██╗██║██╔══██╗██╔══██╗██║     ██║╚══██╔══╝╚══███╔╝{white} |
 {white}|{green} ██║  ██║██║██████╔╝██████╔╝██║     ██║   ██║     ███╔╝ {white} |
 {white}|{green} ██║  ██║██║██╔══██╗██╔══██╗██║     ██║   ██║    ███╔╝  {white} |
 {white}|{green} ██████╔╝██║██║  ██║██████╔╝███████╗██║   ██║   ███████╗{white} |
 {white}|{green} ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝{white} |
 {white}+----------------------{red}<{cyan}@trashz403{red}>{white}-----------------------+{reset}"""
    print(banner)
    
def ctrl_c_handler(signum, frame):
    print(f"\n{red} [{white}+{red}] Ctrl+C detected. Exiting...")
    sys.exit(0)

def brute_force_directories(base_url, wordlist, status_codes, timeout=10, save_to_file=None):
    try:
        with open(wordlist, 'r') as f:
            wordlist_lines = f.readlines()

        with requests.Session() as session:
            output = []  # List to store output for saving to file
            for line in wordlist_lines:
                word = line.strip()
                if not word.startswith("/"):
                    word = "/" + word
                full_url = urljoin(base_url, word)

                try:
                    response = session.get(full_url, timeout=timeout)
                    if response.status_code in status_codes:
                        if response.status_code != 404:
                            result = f"Directory found: {full_url} (Status Code: {response.status_code})"
                            print(green, "[+]", white, result)
                            output.append(result)
                        else:
                            result = f"Page not found: {full_url} (Status Code: {response.status_code})"
                            print(red, "[+]", white, result)
                            output.append(result)
                    else:
                        result = f"Trying: {full_url}"
                        print(white, "[", red, "-", white, "]", result)
                        output.append(result)
                except requests.exceptions.Timeout:
                    result = f"Timeout while accessing '{full_url}' (Request Timeout: {timeout}s)"
                    print(red, "[+]", white, result)
                    output.append(result)
                except requests.exceptions.RequestException as e:
                    result = f"Error occurred while accessing '{full_url}': {e}"
                    print(red, "[+]", white, result)
                    output.append(result)
                    continue

        if save_to_file:
            with open(save_to_file, 'a') as output_file:
                for line in output:
                    output_file.write(line + "\n")
            print(green, "[+]", white, "Results saved to", cyan, save_to_file)
            
    except FileNotFoundError:
        print(red, "[+]", white, f"Wordlist file '{wordlist}' not found.")
        sys.exit(1)
