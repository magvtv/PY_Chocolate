import requests
from bs4 import BeautifulSoup

def celebrity_networth(celebrity_name):
    # construct the link with the celeb's name
    url = f"https://www.celebritynetworth.com/richest-celebrities/{celebrity_name}-net-worth/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    # attempt to fetch the page content
    response = requests.get(url, headers=headers)

    # check the success of the request 
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        networth_element = soup.find("div", class_="value")
        profession_element = soup.find("div", class_="title")
        
        # check if both elements were found in the page
        if networth_element and profession_element:
            networth = networth_element.text.strip()
            profession = profession_element.text.strip()
            return networth, profession
        else:
            # return "Could not retrieve net worth information."
            return None, None
    else:
        # return "Could not retrieve net worth information."
        return None, None

def main():
    celebrity_name = input("Enter celebrity name: ").lower().replace(" ", "-")
    networth, profession = celebrity_networth(celebrity_name)

    # check if the function returned valid data on the celeb
    if networth and profession:
        print(f"Name: {celebrity_name.capitalize().replace('-', ' ')}")
        print(f"Net Worth: {networth}")
        print(f"Profession/Business: {profession}")
    else:
        print(f"Could not retrieve net worth information on {celebrity_name.capitalize().replace('-', ' ')}.")

if __name__ == "__main__":
    main()
