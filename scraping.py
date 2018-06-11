import bs4 as bs
from urllib.request import urlopen

sauce = urlopen("https://en.wikipedia.org/wiki/The_Beatles").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# print(soup.get_text())

# for url in soup.find_all('a'):
#     print(url.get('href'))

# print(nav)

# for url in nav.find_all('a'):
#     print(url.get("href"))

# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

# for div in soup.find_all('div', class_='body'):
#     print(div.text)

table = soup.find('table', class_='infobox')

table_rows = table.find_all('tr')

for tr in table_rows:
    table_header = tr.find_all('th')
    for th in table_header:
        if th.text == "Genres":
            genre_row = tr

genres = [i.text for i in genre_row.find_all('a')]
print(genres)
