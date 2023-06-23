# Generated by Django 4.2.2 on 2023-06-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_profile_comment_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follower_list',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following_list',
        ),
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='main_app.profile'),
        ),
    ]