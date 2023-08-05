#!/bin/python3

import requests

def brute_force_directories(url, wordlist, status_codes, timeout=5):
    try:
        with open(wordlist, 'r') as f:
            wordlist_lines = f.readlines()

        for line in wordlist_lines:
            word = line.strip()
            full_url = f"{url}/{word}"
            try:
                response = requests.get(full_url, timeout=timeout)
                if response.status_code in status_codes:
                    print(f"Directory found: {full_url} (Status Code: {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while accessing '{full_url}': {e}")

    except FileNotFoundError:
        print(f"Wordlist file '{wordlist}' not found.")

def main():
    target_url = input("Enter the URL to brute force directories: ")
    wordlist_file = input("Enter the wordlist file name: ")

    try:
        status_code_range = input("Enter the range of status codes to check (e.g., 200-299): ")
        start_code, end_code = map(int, status_code_range.split('-'))
        status_codes = range(start_code, end_code + 1)
    except ValueError:
        print("Invalid status code range format. Using default range (200-299).")
        status_codes = range(200, 300)

    try:
        timeout = int(input("Enter the timeout (in seconds) for each request (default: 5): "))
    except ValueError:
        print("Invalid timeout value. Using default timeout (5 seconds).")
        timeout = 5

    brute_force_directories(target_url, wordlist_file, status_codes, timeout)

if __name__ == "__main__":
    main()
