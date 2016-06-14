from flask import Flask, render_template
import json

from src import medium

app = Flask(__name__)

@app.route('/')
def home ():
    posts = medium.get_posts(3)
    print posts[1]
    return render_template('home.jinja2', posts=posts)

@app.route('/about')
def about():
    return render_template('about.jinja2')


app.run(debug=app.config['DEBUG'], port=4990)