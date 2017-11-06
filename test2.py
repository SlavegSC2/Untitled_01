#import requests
from bs4 import BeautifulSoup as bs
from clf import keywords
import  db_connector

keywords_dict = keywords(db_connector.corpus,0.005)

wrds = keywords_dict.get(('Наука, техника, образование',))
#print(wrds)
#f = open('index_1.html', 'a')
body_1 = '''<div id="myCanvasContainer">
 <canvas width="600" height="200" id="myCanvas">
  <ul>'''
body_2=''
head = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ru" xml:lang="ru">
<head>
<!--[if lt IE 9]><script type="text/javascript" src="excanvas.js"></script><![endif]-->
<script src="tagcanvas.min.js" type="text/javascript"></script>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" />

</head>'''
tail = '''<script type="text/javascript">
  window.onload = function() {
    try {
  TagCanvas.textColour = '#000000';
  TagCanvas.outlineColour = '#0000CD';
  TagCanvas.minSpeed = 0.02;
  TagCanvas.maxSpeed = 0.15;
  TagCanvas.weight = true;
  TagCanvas.weightMode = 'size';
  TagCanvas.weightSizeMax = 25;
  TagCanvas.weightSizeMin = 10;
  TagCanvas.freezeDecel = true;
  TagCanvas.stretchX = 2;

    TagCanvas.Start('myCanvas');
    } catch(e) {
      // something went wrong, hide the canvas container
      document.getElementById('myCanvasContainer').style.display = 'none';
    }
  };
 </script>

</body>

</html>'''
#f.write(head)
#f.close()
