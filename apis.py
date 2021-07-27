import requests
import pprint
f1=open("index.html",'w')
f2=open("styles.css",'w')
api_key=""
url="https://api.nasa.gov/planetary/apod?api_key="+api_key
r=requests.get(url)
data=r.json()
print(data)
f1.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n<link rel="stylesheet" href="styles.css">\n<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet">\n</head>\n<body>\n<div class="whole-container">\n<div class="heading">\n<h1>Picture of the day<br> </h1>\n</div>\n<div class="main-content">\n<a href='+data['hdurl']+'><img src='+data['url']+' alt="nasa-image"></a>\n<section>\n<h3><u>Information</u><br>'+data['explanation']+'</h3>\n</section>\n</div>\n<footer>\n<h4>&copy; '+data['copyright']+'</h4>\n</footer>\n</div>\n</body>\n</html>\n')
f2.write('img{\nwidth: 70%;\nheight: auto;\n}\nbody{\nfont-family:Lato;\nline-height:2;\nbackground-image: url('+data['url']+');\nbackground-attachment: fixed;\n}\n.whole-container{\ntext-align: center;\nmargin:10rem 5rem 10rem 5rem ;\npadding:10px;\nbackground: rgba( 255, 255, 255, 0.55 );\nbox-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );\nbackdrop-filter: blur( 17.5px );\n-webkit-backdrop-filter: blur( 17.5px );\nborder-radius: 10px;\nborder: 1px solid rgba( 255, 255, 255, 0.18 );\n}\n')
f2.close()
f1.close()
