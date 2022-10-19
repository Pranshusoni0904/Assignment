from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle

# Python Libraries imported to extract web page data, to filter the nesseray data and to convert it to json
import requests
import json
from bs4 import BeautifulSoup
import re

# Get request to get the parsed data of the web page
response_API = requests.get('https://time.com/')
data = BeautifulSoup(response_API.content, 'html.parser')

# 2 list will store the links and the titles of top stories
links, titles = [], []

# Extracting links using find function in beautiful soap
for link in data.find(class_="partial latest-stories").find('ul').find_all('a', attrs={'href': re.compile("/")}):
    links.append(link.get('href'))

# Extracting titles using find function in beautiful soap
all_h3 = data.find_all("h3", class_="latest-stories__item-headline")
for h3 in all_h3:
    titles.append(h3.get_text(strip=True))

# list will append the dict whose keys will be title and link
l = []
for i in range(5):
    d = {
        "title": titles[i],
        "link": links[i]
    }
    l.append(d)

# Finally converting the list into json file
Latest_stories = json.dumps(l)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', data=Latest_stories)


if __name__ == '__main__':
    app.run(debug=True)

# code for running the app
# Python app.py
