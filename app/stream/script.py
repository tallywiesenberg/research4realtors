import tweepy

from app.model import db
from app.stream.auth import api, Auth
import app.stream.streamer
from app.stream.streamer import MyStreamListener

streamer = tweepy.Stream(auth=Auth, listener=MyStreamListener(api=api))

hashtags = ['#realestate', '#realty', '#newhome', '#househunting', '#mortgage', '#foreclosure', '#selling', '#listing',
            '#justlisted', '#openhouse', '#offmarketlisting', '#newlisting', '#homesale', '#homeforsale', '#starterhome', '#starterhome',
            '#renovated', '#homeinspection', '#walkableneighborhood', '#treelinedstreets', '#downtown', '#downtownfrederick', '#frederick',
            '#frederickmd']

streamer.filter(track=hashtags)
