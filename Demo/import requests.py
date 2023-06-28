import requests
from bs4 import BeautifulSoup
 
# Getting page HTML through request
page = requests.get('https://www.samsung.com/id/') 

# Parsing content using beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser') 
 
 # Selecting all of the anchors with titles
links = soup.select("table tbody tr td.titleColumn a") 

# Keep only the first 10 anchors
first10 = links[:10] 
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor