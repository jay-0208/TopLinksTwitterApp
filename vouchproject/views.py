from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import tweepy
import requests
import json
from tweepy import API
from tweepy import OAuthHandler
from datetime import datetime,timedelta

ak = 'eQgwEw5Q6QuMnt8P5o19lk63w'
aks = 'AkbnUZb7Xprd03kI0aG3F4klrHHCoteSOn3ERYZeClvehlnhPZ'



def home(request):
    return render(request ,'front page.html',{})

session={}
def apx(request):
    if request.method == "POST" :
        try:
            auth = OAuthHandler(ak, aks,'https://topapplinkstwitter.herokuapp.com/oauth/complete/twitter')
            redirect_url = auth.get_authorization_url()
            session['request_token'] = auth.request_token
            #print(redirect_url)
            return redirect(redirect_url)
        except:
            return render(request, 'invalid.html', {})



def login1(request):
    try:
        request_token = session['request_token']
        auth = OAuthHandler(ak, aks, 'https://topapplinkstwitter.herokuapp.com/oauth/complete/twitter')
        auth.request_token = request_token
        verifier = request.GET.get('oauth_verifier')
        auth.get_access_token(verifier)
        key,secret = (auth.access_token, auth.access_token_secret)
        auth.set_access_token(key, secret)
        twitter_client = API(auth)

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

        #print(tweets_url_count, tweets_id, tweets_user)

        x = []

        #Modifying tweet embed link as a string

        s = ' class="twitter-tweet tw-align-center"'
        for i in range(len(embed_links)):
            embed_links[i] = embed_links[i][:len(embed_links[i]) - 10]

            if i != 0: x.append('</script>')
            else:      x.append('')

            embed_links[i] = embed_links[i][:11] + s + embed_links[i][11:]
            embed_links[i].replace('\n', '')

            j = 0

            while (j < (len(embed_links[i]) - 1)):
                if ord(embed_links[i][j]) == 92 and embed_links[i][j + 1] == 'n': j += 2
                elif ord(embed_links[i][j]) == 10: j += 1
                else:
                    x[-1] += embed_links[i][j]
                    j += 1


        finaldict = {}
        finaldict['embedlink'] = x
        finaldict['urlcount'] = top_url_counts
        finaldict['topuser'] = top_active_users

        return render(request, 'second page.html', finaldict)



    except Exception as e :
        print(e)
        return render(request,'invalid.html',{})
