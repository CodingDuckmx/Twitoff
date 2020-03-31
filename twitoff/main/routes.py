from flask import Blueprint, render_template
# from twitoff.models import parse_records
from twitoff.tweets.routes import Twuser, Tweet

main = Blueprint('main', __name__)

demo_posts = [
    {
        'author': 'Jesus Caballero',
        'title': 'Blog Blog 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Antonio de la Rosa',
        'title': 'Blog Blog 2',
        'content': 'Second post content',
        'date_posted' : 'April 22, 2018'
    },
]



@main.route('/')
@main.route('/home')
def home():
    
    posts = Tweet.query.all()
    for post in posts[:2]:
        print(post.user_id)
    
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
