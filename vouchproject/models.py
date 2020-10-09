from django.db import models



class TweetsDetails(models.Model):
    unique = models.CharField(max_length=50,primary_key=True, default='.') #Primary key
    user_twitter_id=models.CharField(max_length=25)
    tweet_id=models.CharField(max_length=25)
    tweet_by=models.CharField(max_length=100)
    created_at=models.CharField(max_length=25)
