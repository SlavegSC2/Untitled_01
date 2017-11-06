#для упаковки стэммера
import nltk.stem #стеммер из нлтк (работает так себе, нужно настроить)
from sklearn.feature_extraction.text import CountVectorizer #объект векторизатора (тексты в матрицу типа Слово-употребление)
russian_stemmer=nltk.stem.SnowballStemmer('russian') #посредственный стэммер, но на русском
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer=super(StemmedCountVectorizer,self).build_analyzer()
        #return lambda doc:(russian_stemmer.stem(w) for w in analyzer(doc))#подключаем стеммер к векторизатору
        return lambda doc:(w for w in analyzer(doc))#отключаем стеммер от векторизатору
#----------------------------------------------------------------------------------------------------------------------

#для ключевых слов
import sqlite3
con = sqlite3.connect(r'D:/SQLiteStudio/Data_base')
cur = con.cursor() #
from sklearn.externals import joblib
def keywords(min_tfidf):
    themes = cur.execute('''select NameTheme from Themes''').fetchall()
    themes_norm = [w[0] for w in themes]
    X=joblib.load('vectorizator.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    all_wrds = vectorizer.get_feature_names()
    X_tfidf=joblib.load('vectorizator_tfidf.pkl')
    lst1 = [] # для индексов чтобы получить слова
    lst2 = [] # для тфидф
    lst3 = [] # для списка "слово-тфидф"
    themes_num = (X_tfidf.shape[0])
    res_dict = {}
    for num in range(themes_num):
        a = X_tfidf[num].tocoo()
        for i,word in enumerate(a.data):
            if word>min_tfidf :
                lst1.append(a.col[i])
                lst2.append(a.data[i])
        for item in lst1:
            lst3.append(all_wrds[item])
        result_lst = zip (lst3,lst2)
        res = [w for w in result_lst]
        dict = {themes[num]:res}
        res_dict.update(dict)
        lst1.clear()
        lst2.clear()
        lst3.clear()
        dict.clear()
    return res_dict
#----------------------------------------------------------------------------------------------------------------------
def themes():
    theme = cur.execute('''select NameTheme from Themes''').fetchall()
    theme_norm = [w[0] for w in theme]
    con.close()
    return theme_norm
