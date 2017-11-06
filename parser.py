#coding: cp1251
import feedparser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import sqlite3

con = sqlite3.connect(r'D:/SQLiteStudio/Data_base')

d = feedparser.parse('http://www.warandpeace.ru/ru/rss/')

links=[]
texts = []
themes = []
dates =[]

for item in d.entries:
    link=item.link
    links.append(link)
    date=item.published
    dates.append(date)

for i,link in enumerate(links):
    r = requests.get(link)
    page = bs(r.text, 'lxml')
    page_text = page.find('td', {'class': 'topic_text'}).text
    page_theme = page.find('a', {'class': 'a_topic_info'}).text
    page_date = dates[i]
    cur = con.cursor()
    id = cur.execute('''select idThemes from Themes where NameTheme=(?)''',(page_theme,)).fetchone()
    if id == None :
        cur.execute('''INSERT INTO Themes (NameTheme) VALUES(?)''',(page_theme,))
        id = cur.execute('''select idThemes from Themes where NameTheme=(?)''',(page_theme,)).fetchone()
    con.commit()
    date = cur.execute('''select idTexts from Texts where textDate=(?)''',(page_date,)).fetchone()
    if date == None : cur.execute('''INSERT INTO Texts (textContent, textDate, idNameThemes) VALUES(?,?,?)''',(page_text,page_date,id[0]))
    con.commit()
    print(cur.lastrowid)
    if cur.lastrowid == None : break
con.close()




