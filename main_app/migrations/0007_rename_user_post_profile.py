# Generated by Django 4.2.2 on 2023-06-22 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_comment_likes_user_likes_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='profile',
        ),
    ]
