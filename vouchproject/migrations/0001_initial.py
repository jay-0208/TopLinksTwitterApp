# Generated by Django 3.1.1 on 2020-10-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TweetsDetails',
            fields=[
                ('unique', models.CharField(default='SOME STRING', max_length=50, primary_key=True, serialize=False)),
                ('user_twitter_id', models.CharField(max_length=25)),
                ('tweet_id', models.CharField(max_length=25)),
                ('tweet_by', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=25)),
            ],
        ),
    ]
