import os
from flask import Flask, redirect, render_template, request
import bs4 as bs
from urllib.request import urlopen

app = Flask(__name__)

sauce = urlopen("https://en.wikipedia.org/wiki/The_Beatles").read()
soup = bs.BeautifulSoup(sauce, 'lxml')

band_name = soup.find('h1')

covers = soup.select('table.infobox a.image img[src]')
for cover in covers:
    cover_link = cover['src'] 

table = soup.find('table', class_='infobox')
table_rows = table.find_all('tr')
for tr in table_rows:
    table_header = tr.find_all('th')
    for th in table_header:
        if th.text == "Genres":
            genre_row = tr

genres = [i.text for i in genre_row.find_all('a')]

print(band_name.text)
print(cover_link)
print(genres)

@app.route("/")
def get_index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))