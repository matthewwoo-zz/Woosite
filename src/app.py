from flask import Flask, render_template

from src import medium

app = Flask(__name__)

@app.route('/')
def home ():
    posts = medium.get_posts(3)
    return render_template('home.jinja2', posts=posts)

@app.route('/about')
def about():
    return render_template('about.jinja2')


app.run(debug=app.config['DEBUG'], port=4990)