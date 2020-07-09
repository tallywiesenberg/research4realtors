import tweepy

from app.model import Tweets, db, migrate

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        #Set API
        self.api = api
    def on_status(self, status):
        # Exclude retweets and Tweets w/o geotag
        if ('RT @' not in status.text) and (status.place != None) and (status.place.country_code == 'US'):
            # Choose only geotagged tweets in Frederick County, MD
            longitude = sum([pair[0] for pair in status.place.bounding_box.coordinates[0]])/4
            latitude = sum([pair[1] for pair in status.place.bounding_box.coordinates[0]])/4
            #Frederick County, MD bounding box
            bounding_box = dict(
                upper_right_latitude = 39.7366,
                upper_right_longitude = -77.0961,
                lower_left_latitude = 39.2133,
                lower_left_longitude = -77.6713
            )
            #Locating within Frederick County, MD bounding box
            if (
            (longitude >= bounding_box['lower_left_longitude'])
            and (longitude <= bounding_box['upper_right_longitude'])
            and (latitude  >= bounding_box['lower_left_latitude'])
            and (latitude  <= bounding_box['upper_right_latitude'])):
            #Try to write tweet information to db
                try:
                    try:
                        tweet = Tweets(id=status.id, tweet=status.extended_tweet['full_text'],
                                    username=status.user.screen_name,
                                    realname=status.user.name,
                                    timestamp=status.created_at,
                                    longitude=sum([pair[0] for pair in status.place.bounding_box.coordinates[0]])/4,
                                    latitude=sum([pair[1] for pair in status.place.bounding_box.coordinates[0]])/4)
                        with app.app_context():
                            db.create_all()
                        db.session.add(tweet)
                        db.session.commit()
                        print(status.extended_tweet['full_text'], status.user.location, status.place.name)
                    except AttributeError as e:
                        tweet = Tweets(id=status.id, tweet=status.text,
                                    username=status.user.screen_name,
                                    realname=status.user.name,
                                    timestamp=status.created_at,
                                    longitude=sum([pair[0] for pair in status.place.bounding_box.coordinates[0]])/4,
                                    latitude=sum([pair[1] for pair in status.place.bounding_box.coordinates[0]])/4)
                        with app.app_context():
                            db.create_all()
                        db.session.add(tweet)
                        db.session.commit()
                        print(status.text, status.user.location, status.place.name)
            #if error occurs
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    pass