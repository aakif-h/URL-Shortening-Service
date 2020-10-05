# external libraries
from flask import render_template, Blueprint, jsonify, request, redirect

# internal libraries
from routes.StatusCodes import *
from util import shorten_url
from database.URL import URL, add_URL, get_URL, get_all


pages = Blueprint('pages', __name__)


@pages.route('/', methods=['GET'])
def index():
    try:
        URL_list = get_all()
        url_data = []
        for URL in URL_list:
            url_data.append({"url":URL.url, "short_url":URL.short_url})
        return render_template('index.html', url_data=url_data)
    except Exception as e:
        print(e)
        return jsonify(**{'message': 'Unexpected Error'}), StatusCode_ServerError


@pages.route('/addURL', methods=['POST'])
def add_new_URL():
    try:
        url = request.form['url']
        short_url = shorten_url(url)
        print("Here is the shortened URL:", short_url)
        add_URL(url, short_url)
        return redirect('/')
    except Exception as e:
        print(e)
        return jsonify(**{'message': 'Unexpected Error'}), StatusCode_ServerError


@pages.route('/readShortenedURL', methods=['POST'])
def read_short_URL():
    try:
        short_url = request.form['short_url']
        URL = get_URL(short_url)
        print("True URL: " + URL.url)
        return redirect(URL.url)
    except Exception as e:
        print(e)
        return jsonify(**{'message': 'Unexpected Error'}), StatusCode_ServerError



