wrds = [('гравитацион', 0.0054040225771381243), ('звезд', 0.0056501884692333791), ('слиян', 0.006012527597187233), ('нейтрон', 0.006979628950755646), ('гамм', 0.0063081274357993699), ('всплеск', 0.006012527597187233), ('вспышк', 0.00544902822682537), ('килонов', 0.0052127463173524567), ('lig', 0.0058438775828816318), ('virg', 0.0052127463173524567), ('насеком', 0.0061664929973593696)]
body_1 = '''<body>

<div id="myCanvasContainer">
 <canvas width="600" height="200" id="myCanvas">
  <ul>'''
body_2=''
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

for word in wrds:
    body_2 = body_2 + '<li><a style="font-size: 10pt" href="/'+word[0]+'">'+word[0]+'</a></li>'+'\n'
f = open(r'C:\Users\User\PycharmProjects\untitled2\tagcloud\index_1.html', 'w')
f.write(head+body_1+body_2+tail)
f.close()

diction = {wrds[0]:wrds[0] for wrds in wrds}
