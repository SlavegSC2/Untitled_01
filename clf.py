# coding: cp1251
import sqlite3 #для работы с БД
con = sqlite3.connect(r'D:/SQLiteStudio/Data_base') # устанавливаем подключение к базе
cur = con.cursor() #назначаем курсор для работы БД
from sklearn.externals import joblib #сохранение классификатора

if __name__ == "__main__":
    import db_connector #для получения словарей типа "Тема":[(слово-тфидф)], здесь потому что используется векторизатор
    from sklearn.naive_bayes import MultinomialNB #импортируем Байесовский классификатор
    from functions import StemmedCountVectorizer #импортируем ручной класс с подлюкченным стэммером
    from sklearn.feature_extraction.text import TfidfTransformer
    TFIDFtransformer=TfidfTransformer(sublinear_tf=True, norm='l1', use_idf=True, smooth_idf=False) #объект тфидф векторизатора
    vectorizer = StemmedCountVectorizer(min_df=1, ngram_range=(1,1)) #обычный векторизатор
    Y=vectorizer.fit_transform(db_connector.corpus) #получаем все тексты из базы вида [[тексты одной темы],[тексты другой темы]...[]]
    joblib.dump(vectorizer, 'vectorizer.pkl') #для функции keywords чтобы получить все слова
    joblib.dump(Y,'vectorizator.pkl')
    X=joblib.load('vectorizator.pkl')
    num_samples,num_features=X.shape #информация о массиве количество тем (списков) и слов
    print ('« Вего тем : %d , Всего слов : %d»' % (num_samples,num_features ))
    Y_tfidf=TFIDFtransformer.fit_transform(X) # считаем счеткики тфидф, сопоставляем со словами из векторизатора Х
    joblib.dump(Y_tfidf,'vectorizator_tfidf.pkl')
    X_tfidf=joblib.load('vectorizator_tfidf.pkl')
    themes = cur.execute('''select NameTheme from Themes''' ).fetchall() #получаем названия тем из БД
    clf_y = MultinomialNB(alpha=1).fit(X_tfidf, themes) #сам объект классификатора
    joblib.dump(clf_y,'clf.pkl')
    clf = joblib.load('clf.pkl')
    con.close()
'''
new_post=['Президент России приехал в Москву']
X_new=vectorizer.transform(new_post)
X_new_tfidf=TFIDFtransformer.transform(X_new)
predicted = clf.predict(X_new_tfidf)
print(predicted)
''' #проверка классификатора




