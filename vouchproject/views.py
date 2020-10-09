ak = ''                    #consumer_key
aks = ''                   #consumer_secret_key

from django.shortcuts import render,redirect
import tweepy
import requests
import json
from tweepy import API
from tweepy import OAuthHandler
from datetime import datetime,timedelta





def home(request):
    return render(request ,'front page.html',{})

session={}
def apx(request):
    auth = tweepy.OAuthHandler(ak, aks,'http://localhost:8000/oauth/complete/twitter')
    redirect_url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(redirect_url)



def login1(request):
    try:
        request_token1 = session['request_token']
        del session['request_token']

        auth = OAuthHandler(ak, aks)
        auth.request_token = request_token1

        verifier = request.GET.get('oauth_verifier')
        if verifier is None: return render(request,'invalid.html',{})
        auth.get_access_token(verifier)
        key,secret = auth.access_token, auth.access_token_secret
        auth.set_access_token(key, secret)
        twitter_client = API(auth, wait_on_rate_limit=True)

        tweets_id = []
        tweets_user = {}
        tweets_url_count = {}

        now = datetime.now()

        for tweet in twitter_client.home_timeline():

            if now < (tweet.created_at - timedelta(hours=(24 * 7))): break

            if tweet.entities['urls'] != []:
                #*************** entering into database**********
                try:
                    obj = TweetsDetails()
                    obj.created_at = str(tweet.created_at)[:19]
                    obj.tweet_id = tweet.id
                    obj.tweet_by = tweet.user.screen_name
                    obj.user_twitter_id = myself.screen_name
                    unique_str = myself.screen_name + str(tweet.id)
                    obj.unique = unique_str
                    obj.save()
                except:
                    l = 0

                l = len(tweet.entities['urls'])

                if str(tweet.user.screen_name) in tweets_user:
                    tweets_user[str(tweet.user.screen_name)] += l

                else:
                    tweets_user[str(tweet.user.screen_name)] = l

                for i in range(l):
                    if tweet.entities['urls'][i]['url'] in tweets_url_count:
                        tweets_url_count[tweet.entities['urls'][i]['url']] += 1
                    else:
                        tweets_url_count[tweet.entities['urls'][i]['url']] = 1

                tweets_id.append(int(tweet.id))

        top_url_counts, top_active_users, embed_links = [], [], []

        for x in tweets_url_count.keys():
            top_url_counts.append([tweets_url_count[x], x])

        for x in tweets_user:
            top_active_users.append([tweets_user[x], x])

        for id in tweets_id:
            embReqUrl = 'https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FInterior%2Fstatus%2F' + str(id)
            embResp = requests.get(embReqUrl).json()
            embed_links.append(embResp['html'])

        top_active_users.sort(reverse=True)
        top_url_counts.sort(reverse=True)

        if len(top_active_users) > 3: top_active_users = top_active_users[:3]
        if len(top_url_counts) > 3: top_url_counts = top_url_counts[:3]

        if len(top_active_users) == 0: top_active_users.append(['-', '-'])
        if len(top_url_counts) == 0: top_url_counts.append(['-', '-'])


        x = []

        #Modifying tweet embed link as a string

        s = ' tw-align-center'
        for i in range(len(embed_links)):
            embed_links[i] = embed_links[i][:len(embed_links[i]) - 86]
            embed_links[i] = embed_links[i][:32] + s + embed_links[i][32:]
            x.append(embed_links[i])


        finaldict = {}
        finaldict['embedlink'] = x
        finaldict['urlcount'] = top_url_counts
        finaldict['topuser'] = top_active_users

        return render(request, 'second page.html', finaldict)



    except Exception as e :
        print(e)
        return render(request,'invalid.html',{})
