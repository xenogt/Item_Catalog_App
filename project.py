#!/usr/bin/python

import random
import string
import httplib2
import json
import requests
from functools import wraps
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
from database_setup import Base, Genre, GameItem, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
import os

app = Flask(__name__)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
fkey = os.path.join(THIS_FOLDER, 'fb_client_secrets.json')
gkey = os.path.join(THIS_FOLDER, 'client_secrets.json')
dbpath = os.path.join(THIS_FOLDER, 'gamecatalog.db')

CLIENT_ID = json.loads(
    open(gkey, 'r').read())['web']['client_id']
APPLICATION_NAME = "Genre Game Application"

# Connect to Database and create database session
# engine = create_engine('sqlite:///'+dbpath)
engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# use this decorator to check login status
def login_required(f):
    print 'in login_required'
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    print 'in login method'
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    print 'state: '+state
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token
    app_id = json.loads(open(fkey, 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open(fkey, 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_' \
        'exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' \
        % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    token = result.split(',')[0].split(':')[1].replace('"', '')
    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,' \
        'id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&' \
        'redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;' \
        '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % \
        (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    if result == '{"success":true}':
        del login_session['facebook_id']
    return "you have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    print 'in gconnect'
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets(gkey, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: ' \
        '150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'], 'success')
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    print 'in createuser'
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    print 'in getuserinfo'
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    print 'in gdisconnect'
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['gplus_id']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Genre Information
@app.route('/genre/<int:genre_id>/game/JSON')
def genreGameJSON(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    items = session.query(GameItem).filter_by(
        genre_id=genre_id).all()
    return jsonify(GameItems=[i.serialize for i in items])


@app.route('/genre/<int:genre_id>/game/<int:game_id>/JSON')
def gameItemJSON(genre_id, game_id):
    Game_Item = session.query(GameItem).filter_by(id=game_id).one()
    return jsonify(Game_Item=Game_Item.serialize)


@app.route('/genre/JSON')
def genresJSON():
    genres = session.query(Genre).all()
    return jsonify(genres=[r.serialize for r in genres])


# Show all genres
@app.route('/')
@app.route('/genre/')
def showGenres():
    genres = session.query(Genre).order_by(asc(Genre.name))
    latest = session.query(GameItem).order_by(GameItem.id.desc()) \
        .limit(genres.count())
    if 'username' not in login_session:
        return render_template(
            'publicgenres.html', genres=genres, latest=latest)
    else:
        return render_template('genres.html', genres=genres, latest=latest)


# Create a new genr
@login_required
@app.route('/genre/new/', methods=['GET', 'POST'])
def newGenre():
    if request.method == 'POST':
        newGenre = Genre(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newGenre)
        flash('New Genre %s Successfully Created' % newGenre.name)
        session.commit()
        return redirect(url_for('showGenres'))
    else:
        return render_template('newGenre.html')


# Edit a genre
@login_required
@app.route('/genre/<int:genre_id>/edit/', methods=['GET', 'POST'])
def editGenre(genre_id):
    editedGenre = session.query(
        Genre).filter_by(id=genre_id).one()
    if editedGenre.user_id != login_session['user_id']:
        flash(
            'You are not authorized to edit this genre. Please create your own'
            'genre in order to edit.', 'error')
        return redirect(url_for('showGame', genre_id=genre_id))
    if request.method == 'POST':
        if request.form['name']:
            editedGenre.name = request.form['name']
            flash('Genre Successfully Edited %s' % editedGenre.name, 'success')
            return redirect(url_for('showGenres'))
    else:
        return render_template('editGenre.html', genre=editedGenre)


# Delete a genre
@login_required
@app.route('/genre/<int:genre_id>/delete/', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    genreToDelete = session.query(
        Genre).filter_by(id=genre_id).one()
    if genreToDelete.user_id != login_session['user_id']:
        flash('You are not authorized to delete this genre', 'error')
        return redirect(url_for('showGame', genre_id=genre_id))
    if request.method == 'POST':
        session.delete(genreToDelete)
        flash('%s Successfully Deleted' % genreToDelete.name, 'success')
        session.commit()
        return redirect(url_for('showGenres', genre_id=genre_id))
    else:
        return render_template('deleteGenre.html', genre=genreToDelete)


# Show a genre game
@app.route('/genre/<int:genre_id>/')
@app.route('/genre/<int:genre_id>/game/')
def showGame(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    creator = getUserInfo(genre.user_id)

    items = session.query(GameItem).filter_by(
        genre_id=genre_id).all()

    if 'username' not in login_session:
        return render_template(
            'publicgame.html', items=items, genre=genre, creator=creator)
    else:
        return render_template(
            'game.html', items=items, genre=genre, creator=creator)


# Create a new game item
@login_required
@app.route('/genre/<int:genre_id>/game/new/', methods=['GET', 'POST'])
def newGameItem(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        newItem = GameItem(
            name=request.form['name'],
            description=request.form['description'],
            release_year=request.form['release_year'],
            platform=request.form['platform'],
            genre_id=genre_id,
            user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash(
            'New Game %s Item Successfully Created' % (newItem.name),
            'success')
        return redirect(url_for('showGame', genre_id=genre_id))
    else:
        return render_template('newgameitem.html', genre_id=genre_id)


# show a game item
@app.route(
    '/genre/<int:genre_id>/game/<int:game_id>/view', methods=['GET', 'POST'])
def showSingleGame(genre_id, game_id):
    toViewItem = session.query(GameItem).filter_by(id=game_id).one()
    creator = getUserInfo(toViewItem.user.id)
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if 'user_id' not in login_session:
        return render_template(
            'publicsinglegame.html',
            item=toViewItem, genre=genre, creator=creator)
    if toViewItem.user.id != login_session['user_id']:
        return render_template(
            'publicsinglegame.html',
            item=toViewItem, genre=genre, creator=creator)
    else:
        return render_template(
            'singlegame.html', item=toViewItem, genre=genre, creator=creator)


# Edit a game item
@login_required
@app.route(
    '/genre/<int:genre_id>/game/<int:game_id>/edit', methods=['GET', 'POST'])
def editGameItem(genre_id, game_id):
    editedItem = session.query(GameItem).filter_by(id=game_id).one()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if login_session['user_id'] != editedItem.user_id:
        flash('You are not authorized to edit this game item', 'error')
        return redirect(url_for('showGame', genre_id=genre_id))
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['release_year']:
            editedItem.release_year = request.form['release_year']
        if request.form['platform']:
            editedItem.platform = request.form['platform']
        session.add(editedItem)
        session.commit()
        flash('Game Item Successfully Edited', 'success')
        return redirect(url_for('showGame', genre_id=genre_id))
    else:
        return render_template(
            'editgameitem.html',
            genre_id=genre_id, game_id=game_id, item=editedItem)


# Delete a game item
@login_required
@app.route(
    '/genre/<int:genre_id>/game/<int:game_id>/delete', methods=['GET', 'POST'])
def deleteGameItem(genre_id, game_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    itemToDelete = session.query(GameItem).filter_by(id=game_id).one()
    if login_session['user_id'] != itemToDelete.user_id:
        flash('You are not authorized to delete this game item.', 'error')
        return redirect(url_for('showGame', genre_id=genre_id))
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Game Item Successfully Deleted', 'success')
        return redirect(url_for('showGame', genre_id=genre_id))
    else:
        return render_template('deleteGameItem.html', item=itemToDelete)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            print(gdisconnect())
        if login_session['provider'] == 'facebook':
            print(fbdisconnect())
        del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showGenres'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showGenres'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
