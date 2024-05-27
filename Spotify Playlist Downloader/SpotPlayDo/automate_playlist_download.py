import time
import json
from playwright.sync_api import sync_playwright


def download_song(song_link):
    with sync_playwright() as p:
        # launch brave to accomplish sequential actions
        browser = p.chromium.launch(executable_path="/snap/bin/brave", headless=False)
        page = browser.new_page()
        page.goto("https://spotifydown.com/")
        
        search_box = page.locator("input[name='query']")
        search_box.fill(song_link)
        search_box.press("Enter")

        # wait for the search results to load
        page.wait_for_selector("text=Download")
        
        # wait for download button to be visible on page then press download action
        download_button = page.locator("text=Download").first
        download_button.click()
        
        # wait 15s for download to complete
        time.sleep(15000)
        browser.close()
        
if __name__ == '__main__':
    with open('songs.json', 'r') as file:
        songs = json.load(file)
    for song in songs:
        download_song(song['spotify_song_link'])
        
        
        
