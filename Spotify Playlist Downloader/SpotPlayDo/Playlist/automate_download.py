import time
import json
from playwright.sync_api import sync_playwright


def download_song(page, song_link):
    try:
        print("Navigating to spotidown website")
        page.goto("https://spotifydown.com/")
        
        print("Filling in the search box")
        search_box = page.locator("input[name='query']")
        search_box.fill(song_link)
        search_box.press("Enter")

        # wait for the search results to load
        page.wait_for_selector("text=Download")
        
        # wait for download button to be visible on page then press download action
        download_button = page.locator("text=Download").first
        download_button.click()
        
        # wait 15s for download to complete
        print("Awaiting song mp3 download to start")
        page.wait_for_timeout(5000)
    except Exception as e:
        print(f"Error has occurred:\n{e}")
        
if __name__ == '__main__':
    with open('songs.json', 'r') as file:
        songs = json.load(file)
        
    with sync_playwright() as p:
     # launch brave once to accomplish sequential actions in download_song function
     browser = p.chromium.launch(executable_path="/snap/bin/brave", headless=False)
     page = browser.new_page()
     
     song_count = len(songs)
     index = 0
     
     while index < song_count:
        song = songs[index]
        print(f"Downloading:\n{song['title']} by {song['artist']}")
        download_song(page, song['spotify_song_link'])
        index += 1
    
    browser.close()
    print("Browser has been closed!")
        
        
        
