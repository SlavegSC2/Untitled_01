# coding: cp1251
import sqlite3 #��� ������ � ��
con = sqlite3.connect(r'D:/SQLiteStudio/Data_base') # ������������� ����������� � ����
cur = con.cursor() #��������� ������ ��� ������ ��
from sklearn.externals import joblib #���������� ��������������

if __name__ == "__main__":
    import db_connector #��� ��������� �������� ���� "����":[(�����-�����)], ����� ������ ��� ������������ ������������
    from sklearn.naive_bayes import MultinomialNB #����������� ����������� �������������
    from functions import StemmedCountVectorizer #����������� ������ ����� � ������������ ���������
    from sklearn.feature_extraction.text import TfidfTransformer
    TFIDFtransformer=TfidfTransformer(sublinear_tf=True, norm='l1', use_idf=True, smooth_idf=False) #������ ����� �������������
    vectorizer = StemmedCountVectorizer(min_df=1, ngram_range=(1,1)) #������� ������������
    Y=vectorizer.fit_transform(db_connector.corpus) #�������� ��� ������ �� ���� ���� [[������ ����� ����],[������ ������ ����]...[]]
    joblib.dump(vectorizer, 'vectorizer.pkl') #��� ������� keywords ����� �������� ��� �����
    joblib.dump(Y,'vectorizator.pkl')
    X=joblib.load('vectorizator.pkl')
    num_samples,num_features=X.shape #���������� � ������� ���������� ��� (�������) � ����
    print ('� ���� ��� : %d , ����� ���� : %d�' % (num_samples,num_features ))
    Y_tfidf=TFIDFtransformer.fit_transform(X) # ������� �������� �����, ������������ �� ������� �� ������������� �
    joblib.dump(Y_tfidf,'vectorizator_tfidf.pkl')
    X_tfidf=joblib.load('vectorizator_tfidf.pkl')
    themes = cur.execute('''select NameTheme from Themes''' ).fetchall() #�������� �������� ��� �� ��
    clf_y = MultinomialNB(alpha=1).fit(X_tfidf, themes) #��� ������ ��������������
    joblib.dump(clf_y,'clf.pkl')
    clf = joblib.load('clf.pkl')
    con.close()
'''
new_post=['��������� ������ ������� � ������']
X_new=vectorizer.transform(new_post)
X_new_tfidf=TFIDFtransformer.transform(X_new)
predicted = clf.predict(X_new_tfidf)
print(predicted)
''' #�������� ��������������




