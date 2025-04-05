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
    print(ratio)  # Check the similarity of the two strings

if __name__ == "__main__":
    url1 = input("Enter the URL of the first webpage: ")
    url2 = input("Enter the URL of the second webpage: ")
    compare_webpages(url1, url2)