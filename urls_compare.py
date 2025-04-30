import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def fetch_webpage_content(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def compare_webpages(url1, url2):
    """Compares the content of two webpages and prints the differences."""
    content1 = fetch_webpage_content(url1)
    content2 = fetch_webpage_content(url2)

    if content1 is None or content2 is None:
        return

    soup1 = BeautifulSoup(content1, 'html.parser')
    soup2 = BeautifulSoup(content2, 'html.parser')

    text1 = soup1.get_text().splitlines()
    text2 = soup2.get_text().splitlines()

    seq_match = SequenceMatcher(None, text1, text2)
    ratio = seq_match.ratio()
    print("----------------------------------------------------------")
    print(url1)
    print(url2)
    print(ratio)  # Check the similarity of the two strings
    print("----------------------------------------------------------")

def fetch_urls(file_path):
    """
    Reads lines from a text file and returns them as an array.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: An array containing the lines from the file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove trailing newline characters from each line
            lines = [line.rstrip('\n') for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file1 = input("Enter the URL of the first webpage: ")
    file2 = input("Enter the URL of the second webpage: ")
    urls_list1 = fetch_urls(file1)
    urls_list2 = fetch_urls(file2)
    if len(urls_list1) != len(urls_list2):
        print("urls'  Lists lengths mismatch!")
    else:
        for i in range(0,len(urls_list1)):
            compare_webpages(urls_list1[i], urls_list2[i])
    