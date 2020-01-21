import requests
from bs4 import BeautifulSoup
import  _sqlite3
#import  re

def createTable():
    con.execute("CREATE TABLE IF NOT EXISTS Top250(Title TEXT, ReleaseDate INT, Rating REAL)")

#def addValue():


con = _sqlite3.connect("imdb.db")
cursor = con.cursor()

r = requests.get("https://www.imdb.com/chart/top/")

soup = BeautifulSoup(r.content, "html.parser")

var = soup.find_all("tbody", {"class":"lister-list"})

var = var[0].find_all("tr")

film_arr = []

#print("----------- TOP 250 -----------")

for film in var:
    filmbasliklari = (film.find_all("td", {"class":"titleColumn"}))
    film_ismi = filmbasliklari[0].text
    film_ismi = film_ismi.replace("\n","")

    #print (re.findall(r"[\w']+", film_ismi))

    #film_arr = film_ismi.split(".      ")
    #txt = film_arr[1]
    #print(int(txt[txt.find('(')+1 : txt.find(')')])) # Filmin cikis tarihini cekiyor
    #print((txt.split("("))[0])


    #deger = (film.find_all("td", {"class": "ratingColumn imdbRating"}))
    #rating = deger[0].text
    #rating = rating.replace("\n","")

