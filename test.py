import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineSettings


class MyWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, nav_type, is_frame):
        if nav_type == 0:
            print(url)
            return False
        else:
            print(url)
            return True

if __name__ == '__main__':
    app = QApplication([])
    url = "file:///C:/Users/User/PycharmProjects/untitled2/tagcloud/index_1.html"
    p = MyWebEnginePage()
    v = QWebEngineView()
    v.setPage(p)
    v.setUrl(QUrl(url))
    v.show()
    app.exec_()


