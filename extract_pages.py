import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_all_pages(url, visited=None):
    if visited is None:
        visited = set()
    
    if url in visited:
        return []
    
    visited.add(url)
    pages = [url]
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            if absolute_url.startswith(url):
                pages.extend(extract_all_pages(absolute_url, visited))
    
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
    
    return list(set(pages))

if __name__ == '__main__':
    website_url = input("Enter the website URL to extract all pages: ")
    all_pages = extract_all_pages(website_url)
    
    print("All pages found:")
    for page in all_pages:
        print(page)