from decouple import config
from flask import Flask, render_template, render_template_string

from .model import db, Tweets


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def root():
        tweets = Tweets.query.all()
        return render_template('base.html', tweets=tweets)

    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template_string('Database reset!')

    return app