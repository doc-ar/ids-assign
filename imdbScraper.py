import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

fp = open('MovieLinks.txt')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
URLList = []

# Make a list of all URLs
for line in fp.readlines():
    URLList.append(line.strip()) # strip() is used to remove the trailing characters that might interfere in making requests
fp.close()

# Iterate through the links and create a dictionary item for each movie (URL, Name and Rating)
# Append each movie's dictionary item to the movies list
movies = []
for link in URLList:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    movie = {}
    movie['URL'] = link
    movie['Name'] = soup.find('span', attrs={'class':'sc-afe43def-1 fDTGTb'}).text
    rating = soup.find('span', attrs={'class':'sc-bde20123-1 iZlgcd'}).text
    movie['Rating'] = float(rating)
    movies.append(movie)
    time.sleep(1)

# Create a dataframe from the list 'movies' which stores all movie details as dictionaries
df = pd.DataFrame.from_dict(movies)
# Export the Scraped data as an excel file
df.to_excel('Movies.xlsx')