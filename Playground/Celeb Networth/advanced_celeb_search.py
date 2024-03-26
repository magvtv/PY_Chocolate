from googlesearch import search
import requests
from bs4 import BeautifulSoup

def find_celeb_networth_pages(celebrity_name):
    query = f"{celebrity_name} net worth"
    for j in search(query, num_results=10):
        yield j
        
def scrape_networth(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # will customize this part based on the structure of the page scraped
            # an example and likely won't work without adjustments
            networth_element = soup.find("div", class_="netWorth")
            if(networth_element):
                return networth_element.text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def main():
    celebrity_name = input("Enter celebrity's name: ")
    for url in find_celeb_networth_pages(celebrity_name):
        networth = scrape_networth(url)
        if networth:
            print(f"Found net worth information: {networth}")
            break
        else:
            print("Can't find net worth info")
            
if __name__ == "__main__":
    main()