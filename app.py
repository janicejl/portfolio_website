from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
  return render_template('hello.html', name=name)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)
