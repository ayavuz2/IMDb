import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top/")

soup = BeautifulSoup(r.content, "html.parser")

var = soup.find_all("tbody", {"class":"lister-list"})

var = var[0].find_all("tr")

print("----------- TOP 250 -----------")

for film in var:
    filmbasliklari = (film.find_all("td", {"class":"titleColumn"}))
    film_ismi = filmbasliklari[0].text
    film_ismi = film_ismi.replace("\n","")
    print(film_ismi)
