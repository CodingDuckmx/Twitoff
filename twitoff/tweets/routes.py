from flask import Blueprint, render_template, jsonify, url_for, redirect

from twitoff.models import db, Twuser, Tweet, parse_records
from twitoff.services.twitter_services import twitter_api
from twitoff.services.basilica_services import basilica_api_client
from twitoff.tweets.forms import SearchTwitterUser


twitter_api_client = twitter_api()

twitter_routes = Blueprint('twitter_routes', __name__)

def store_twitter_user_data(screen_name=None):
    print(screen_name)

    twitter_user = twitter_api_client.get_user(screen_name)

    #Find or create database user (entry):

    db_twuser = Twuser.query.get(twitter_user.id) or Twuser(id=twitter_user.id)
    db_twuser.screen_name = twitter_user.screen_name
    db_twuser.name = twitter_user.name
    db_twuser.location = twitter_user.location
    db_twuser.followers_count = twitter_user.followers_count
    db.session.add(db_twuser)
    db.session.commit()


    # Get tweets (statuses)

    statuses = twitter_api_client.user_timeline(screen_name, tweet_mode='extended', count=42, exclude_replies=True, include_rts=False)

    # Transform the data via Basilica
    print('Status count:', len(statuses))
    basilica_api = basilica_api_client()
    all_statuses_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_api.embed_sentences(all_statuses_texts, model='twitter'))
    print('Number of embeddings:', len(embeddings))

    # breakpoint()

    counter = 0
    for status in statuses:
        print(status.full_text)
        print('----')

        #Find or create the database tweet row:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id 
        db_tweet.full_text = status.full_text
        embedding = embeddings[counter]
        # print(embedding)
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        counter +=1
    db.session.commit()


    return  db_twuser, statuses


@twitter_routes.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchTwitterUser()
    if form.validate_on_submit():
        db_twuser, statuses = store_twitter_user_data(screen_name=form.twname.data)
        return render_template('user-tweets.html', twuser=db_twuser, statuses=statuses)
        
    return render_template('search.html', title='Search', form=form)


@twitter_routes.route('/users.json')
def list_users():
    db_twuser = Twuser.query.all()
    twusers_parced = parse_records(db_twuser)
    return jsonify(twusers_parced)




