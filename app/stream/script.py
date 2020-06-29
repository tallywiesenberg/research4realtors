import tweepy

import ..auth
from ..auth import api, Auth
import streamer
from streamer import MyStreamListener

streamer = tweepy.Stream(auth=Auth, listener=MyStreamListener)

hashtags = ['#realestate', '#realty', '#newhome', '#househunting', '#mortgage', '#foreclosure', '#selling', '#listing',
            '#justlisted', '#openhouse', '#offmarketlisting', '#newlisting', '#homesale', '#homeforsale', '#starterhome', '#starterhome',
            '#renovated', '#homeinspection', '#walkableneighborhood', '#treelinedstreets', '#downtown', '#downtownfrederick', '#frederick',
            '#frederickmd']

streamer.filter(track=hashtags)
    