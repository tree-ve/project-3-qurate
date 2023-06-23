# Generated by Django 4.2.2 on 2023-06-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_follow_list_profile_follower_list_delete_follows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comment_likes',
            field=models.ManyToManyField(blank=True, related_name='comments_liked', to='main_app.comment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower_list',
            field=models.ManyToManyField(blank=True, to='main_app.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following_list',
            field=models.ManyToManyField(blank=True, through='main_app.Follow_List', to='main_app.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='post_likes',
            field=models.ManyToManyField(blank=True, related_name='posts_liked', to='main_app.post'),
        ),
    ]