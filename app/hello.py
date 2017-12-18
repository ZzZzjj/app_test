from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello,%s!</h1>'% name
	
if __name__ == '__main__':
	app.run(port=8788,debug=True)