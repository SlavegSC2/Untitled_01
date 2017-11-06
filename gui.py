# coding utf-8
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import sys
import keyword_dicts_processing, functions
import resources
from PyQt5.QtCore import QUrl, pyqtSignal
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
    from PyQt5.QtWebEngineWidgets import QWebEnginePage
    from PyQt5.QtWebEngineWidgets import QWebEngineSettings
    from PyQt5.QtWebEngineWidgets import QWebEngineProfile
    from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
except ImportError:
    from PyQt5.QtWebKit import QWebView
    from PyQt5.QtWebKit import QWebSettings

class MyWebEnginePage(QWebEnginePage):
    link_clicked = pyqtSignal(str)
    global prev_url
    prev_url = [QUrl('file:///C:/килонов')]
    def acceptNavigationRequest(self, url, nav_type, is_frame):
        if nav_type == 0:
            if url != prev_url[-1]:
                self.link_clicked.emit(str(url))
            prev_url.append(url)
            return False
        else:

            return True

class Browser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global themes
        themes = functions.themes()
        global diction
        diction = keyword_dicts_processing.diction
        self.initUi()
        self.initSignals()

    def initUi(self):
        loadUi('untitled.ui', self)
        self.page = MyWebEnginePage()
        self.webEngineView.setPage(self.page)
        for theme in themes:
            self.listWidget.addItem(theme)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('C:/Users/Admin/PycharmProjects/untitled2/img/down_arr.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('C:/Users/Admin/PycharmProjects/untitled2/img/del.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap('C:/Users/Admin/PycharmProjects/untitled2/img/top_arr.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap('C:/Users/Admin/PycharmProjects/untitled2/img/srch.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)

    def initSignals(self):
        self.listWidget.itemClicked.connect(self.on_list_query)
        self.page.link_clicked.connect(self.LWchange)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.up)
        self.pushButton.clicked.connect(self.down)
        self.pushButton_3.clicked.connect(self.search)

    def LWchange(self,url):
        url1 = url.split('/C:')
        norm_url = url1[1][1:len(url[1])-3]
        self.listWidget_2.addItem(diction.get(norm_url))

    def on_list_query(self,item):
        theme_name = item.text().replace(':',' -')
        url = "file:///C:/Users/Admin/PycharmProjects/untitled2/tagcloud/'"+theme_name+".html"
        self.webEngineView.load(QUrl(url))

    def delete(self):
        for item in self.listWidget_2.selectedItems():
            row = self.listWidget_2.row(item)
            self.listWidget_2.takeItem(row)

    def up(self):
        for item in self.listWidget_2.selectedItems():
            row = self.listWidget_2.row(item)
            curent_item = self.listWidget_2.takeItem(row)
            self.listWidget_2.insertItem(row-1,curent_item)

    def down(self):
        for item in self.listWidget_2.selectedItems():
           row = self.listWidget_2.row(item)
           curent_item = self.listWidget_2.takeItem(row)
           self.listWidget_2.insertItem(row+1,curent_item)

    def search(self):
        items = []
        qry = ''
        for index in range(self.listWidget_2.count()):
            items.append(self.listWidget_2.item(index))
        for item in items:
            qry = qry + item.text() + ' '
        url = "https://www.google.co.in/search?q=" +qry+ "&oq="+qry+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
        self.webEngineView_2.load(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    browser = Browser()
    browser.show()
    sys.exit(app.exec_())