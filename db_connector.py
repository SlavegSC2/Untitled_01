import sqlite3
con = sqlite3.connect(r'D:/SQLiteStudio/Data_base')
corpus = []
cur = con.cursor()
themes = cur.execute('''select idThemes from Themes''' ).fetchall() #получаем id тем
for theme in themes:
    text = ''
    theme_num = theme[0] #ай ди темы первый элемент полученного кортежа
    texts = cur.execute('''select textContent from Texts where idNameThemes=(?)''',(theme_num,)).fetchall() #полуачем тексты с соотвветствующим айди
    for txt in texts:
        txt_norm = txt[0].replace('\xa0','')
        text=text+txt_norm #собираем тексты одной темы в одну строку
    corpus.append(text) #добавляем строку в список. При следующей итерации в список добавится строка уже другой темы и т.п.
#print(corpus)
con.close()


#здесь получаем тексты из базы и возвращаем их списком по темам