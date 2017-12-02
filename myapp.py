from flask import Flask,render_template,request
from requests import post
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/',methods=('GET','POST'))
def index():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		word = request.form.get('word')
		sizes = request.form.get('sizes')
		fonts = request.form.get('fonts')
		fontcolor = request.form.get('fontcolor')
		data = {
			'word':word,
			'sizes':sizes,
			'fonts':fonts,
			'fontcolor':fontcolor,
		}
		html = post('http://www.uustv.com/',data=data).text
		dom = BeautifulSoup(html,"html.parser")
		img_url = dom.find_all('div','tu')[0].img['src']
		apath = 'http://www.uustv.com/' + img_url
		return render_template('index.html',apath=apath)
if __name__== "__main__":
	app.run(debug=True,port=80)