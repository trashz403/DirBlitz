#!/usr/bin/env python3

import sys
import requests
import signal

# Copyright (c) 2023 GH05T-HUNTER5. All rights reserved.

green = "\033[92m"
cyan = "\033[36m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"

# Banner
def print_banner():
    banner = f"""
 {white}+---------------------------------------------------------+
 {white}|{green} ██████╗ ██╗██████╗ ██████╗ ██╗     ██╗████████╗███████╗{white} |
 {white}|{green} ██╔══██╗██║██╔══██╗██╔══██╗██║     ██║╚══██╔══╝╚══███╔╝{white} |
 {white}|{green} ██║  ██║██║██████╔╝██████╔╝██║     ██║   ██║     ███╔╝ {white} |
 {white}|{green} ██║  ██║██║██╔══██╗██╔══██╗██║     ██║   ██║    ███╔╝  {white} |
 {white}|{green} ██████╔╝██║██║  ██║██████╔╝███████╗██║   ██║   ███████╗{white} |
 {white}|{green} ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝{white} |
 {white}+-----------------------{cyan}trashz403{white}-------------------------+{reset}"""
    print(banner)

def ctrl_c_handler(signum, frame):
    print(f"\n{red} [{white}+{red}] Ctrl+C detected. Exiting...")
    sys.exit(0)

def ctrl_d_handler(signum, frame):
    print(f"\n{red} [{white}+{red}] Ctrl+D detected. Exiting...")
    sys.exit(0)

def brute_force_directories(url, wordlist, status_codes, timeout=5):
    try:
        with open(wordlist, 'r') as f:
            wordlist_lines = f.readlines()

        with requests.Session() as session:
            for line in wordlist_lines:
                word = line.strip()
                full_url = f"{url}/{word}"
                try:
                    response = session.get(full_url, timeout=timeout)
                    if response.status_code in status_codes:
                        if "404" not in response.text:
                            print(fr"{green} [{white}+{green}] Directory found: {full_url} (Status Code: {response.status_code})")
                except requests.exceptions.Timeout:
                    print(fr"{red} [{white}+{red}] Timeout while accessing '{full_url}'")
                except requests.exceptions.RequestException as e:
                    print(fr"{red} [{white}+{red}] Error occurred while accessing '{full_url}': {e}")
                    continue

    except FileNotFoundError:
        print(fr"{green} [{white}+{green}] Wordlist file '{wordlist}' not found.")
        sys.exit(1)

def main():
    try:
        print_banner()
        target_url = input(f"{green} [{white}+{green}] Enter the URL to brute force directories: ").rstrip('/')
        wordlist_file = input(f"{green} [{white}+{green}] Enter the wordlist file name: ")

        try:
            status_code_range = input(f"{green} [{white}+{green}] Enter the range of status codes to check (e.g., 200-299): ")
            start_code, end_code = map(int, status_code_range.split('-'))
            status_codes = range(start_code, end_code + 1)
        except ValueError:
            print(fr"{red} [{white}+{red}] Invalid status code range format. {green}Using default range (200-299).")
            status_codes = range(200, 300)

        try:
            timeout = int(input(f"{green} [{white}+{green}] Enter the timeout (in seconds) for each request (default: 5): "))
        except ValueError:
            print(f"{red} [{white}+{red}] Invalid timeout value.{green} Using default timeout (5 seconds).")
            timeout = 5

        signal.signal(signal.SIGINT, ctrl_c_handler)
        signal.signal(signal.SIGQUIT, ctrl_d_handler)

        brute_force_directories(target_url, wordlist_file, status_codes, timeout)

    except KeyboardInterrupt:
        print(f"{green} [{white}+{green}] Brute force process interrupted.")
        sys.exit(0)

if __name__ == "__main__":
    main()
