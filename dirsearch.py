# Creator TRASHZ403 
# @trashz403 -instagram 
# @trashz403 -twitter
# @trashz403 everywhere exept facebook XD😂
# please follow I will follow you back for sure:)
import requests

def brute_force_directories(url, wordlist):
    try:
        with open(wordlist, 'r') as f:
            wordlist_lines = f.readlines()

        for line in wordlist_lines:
            word = line.strip()
            full_url = f"{url}/{word}"
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Directory found: {full_url}")

    except requests.exceptions.RequestException:
        print("Error occurred while brute-forcing directories.")
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist}' not found.")

def main():
    target_url = input("Enter the URL to brute force directories: ")
    wordlist_file = input("Enter the wordlist file name: ")
    brute_force_directories(target_url, wordlist_file)

if __name__ == "__main__":
    main()

