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
from validlink import check_url_validity
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
def main():
    try:
        # ... (previous code remains the same)
        print_banner()
        print(f"{white} |{green} This script is for educational purposes only.          {white} |")
        print(f"{white} |{green} Use responsibly and only on systems you have permission {white}|")
        print(f"{white} |{green} to test against. Be aware of local laws and regulations.{white}|")
        print(f"{white} +---------------------------------------------------------+{reset}")

        base_url = input(f"{green} [{white}+{green}] Enter the base URL (e.g., https://example.com) {white}:{green} ").rstrip('/')
        is_valid = check_url_validity(base_url)
        if is_valid:
            pass
        else:
            print(f"{red} [{white}+{red}]The URL {base_url} is not valid.")
            exit()
        wordlist_file = input(f"{green} [{white}+{green}] Enter the wordlist file name {white}:{green} ")
        try:
            status_code_range = input(f"{green} [{white}+{green}] Enter the range of status codes to check (e.g., 200-299) {white}:{green} ")
            if not status_code_range:
                status_codes = range(200, 300)
            else:
                start_code, end_code = map(int, status_code_range.split('-'))
                status_codes = range(start_code, end_code + 1)
        except ValueError:
            status_codes = range(200, 300)
        try:
            timeout_input = input(f"{green} [{white}+{green}] Enter the timeout (in seconds) for each request (default: 5) {white}:{green} ")
            timeout = int(timeout_input) if timeout_input else 5
        except ValueError:
            timeout = 5
        save_results = input(f"{green} [{white}+{green}] Do you want to save the results to a .txt file? (y/n) {white}:{green} ").strip().lower()
        if save_results == 'y':
            result_file = input(f"{green} [{white}+{green}] Enter the filename to save results (example.txt) : {white}:{green} ")
        elif save_results == "n":
            result_file = None
            
        else:
            print("Invalid input!")

        signal.signal(signal.SIGINT, ctrl_c_handler)

        brute_force_directories(base_url, wordlist_file, status_codes, timeout, save_to_file=result_file)

        print(f"{green} [{white}+{green}] Directory finding script completed." + reset)

    except KeyboardInterrupt:
        print(f"{green} [{white}+{green}] Brute force process interrupted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
