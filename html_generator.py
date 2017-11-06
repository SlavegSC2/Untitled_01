from keyword_dicts_processing import wrds as wrds
#__________________________________________________Статика______________________________________________________________
body_1 = '''<body>
<div id="myCanvasContainer">
 <canvas width="600" height="200" id="myCanvas">
  <ul>'''
head = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ru" xml:lang="ru">
<head>
<!--[if lt IE 9]><script type="text/javascript" src="excanvas.js"></script><![endif]-->
<script src="tagcanvas.min.js" type="text/javascript"></script>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251" />
</head>
'''
tail = '''</ul>
 </canvas>
</div>
<script type="text/javascript">
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
#----------------------------------------------------------------------------------------------------------------------
#____________________________________________генерация страниц для облака тэгов________________________________________
for list in wrds:
    body_2=''
    name = list[0]
    for word in list[1]:
        #print(word)
        body_2 = body_2 + '<li><a style="font-size: 10pt" href="/'+word[0]+'">'+word[0]+'</a></li>'+'\n'
    name_norm = name.replace(':',' -')
    f = open(r'C:\Users\Admin\PycharmProjects\untitled2\tagcloud\''+name_norm+'.html', 'w')
    f.write(head+body_1+body_2+tail)
    f.close()

