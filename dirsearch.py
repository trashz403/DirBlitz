import requests

def brute_force_directories(url, wordlist, status_codes):
    try:
        with open(wordlist, 'r') as f:
            wordlist_lines = f.readlines()

        for line in wordlist_lines:
            word = line.strip()
            full_url = f"{url}/{word}"
            response = requests.get(full_url)
            if response.status_code in status_codes:
                print(f"Directory found: {full_url} (Status Code: {response.status_code})")

    except requests.exceptions.RequestException:
        print("Error occurred while brute-forcing directories.")
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

    brute_force_directories(target_url, wordlist_file, status_codes)

if __name__ == "__main__":
    main()
  
