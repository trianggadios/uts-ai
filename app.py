from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import session

from module import model_config

from gensim.models import Doc2Vec

import pickle
import gensim
import tweepy
import datetime

app = Flask(__name__)

api_key = "lrRxfrV5n4AudieQDnl7BsX50"
api_secret_key = "dPF86YYwFFTunkWL8TrQu3rRo3p13eRIevX3RKkOHkw2XCafCZ"
access_token = "1389444564054810632-PXJiEIbHJv6eHK22LdL4zHd2A9TtO5"
access_token_secret = "SGHgDBKQxQv0fxe80RE4GfMb6IrrcW22FeFoBY4NCNCAl"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download_model', methods=['GET'])
def model_doc2vec_download():
    try:
        model_config.download_all_model()
        global doc2vec_model
        global clf_randomforest_model
        doc2vec_model = Doc2Vec.load('model/model.d2v')
        clf_randomforest_model = pickle.load(open('model/model_final.sav', 'rb'))
        return jsonify(
            {
                'status': 200,
                'message': 'success download'
            }
        )
    except Exception as e:
        return jsonify(
            {
                'status': 500,
                'message': f'{e}. Please refresh webpage'
            }
        )


@app.route('/analisis', methods=['POST'])
def analisis_data():
    username = request.form['username']

    startDate = datetime.datetime(2021, 5, 3, 0, 0, 0)
    endDate = datetime.datetime(2021, 5, 4, 0, 0, 0)

    tweets = []
    try:
        tmpTweets = api.user_timeline(username, count=100)
    except:
        return 'api sudah mencapai batas'
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet.text)

    positif = []
    negatif = []

    for messages in tweets:
        normalize_messages = gensim.utils.simple_preprocess(messages)
        vector_messages = doc2vec_model.infer_vector(normalize_messages)
        result = clf_randomforest_model.predict([vector_messages])[0]
        if result == 1:
            positif.append(messages)
        else:
            negatif.append(messages)

    return f"dari {len(tweets)} tweets terdapat {len(positif)} tweets positif, dan {len(negatif)} tweets negatif"
