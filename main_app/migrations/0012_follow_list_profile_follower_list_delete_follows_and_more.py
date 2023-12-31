# Generated by Django 4.2.2 on 2023-06-22 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_comment_likes_alter_post_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='follower_list',
            field=models.ManyToManyField(to='main_app.profile'),
        ),
        migrations.DeleteModel(
            name='Follows',
        ),
        migrations.AddField(
            model_name='follow_list',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following_list',
            field=models.ManyToManyField(through='main_app.Follow_List', to='main_app.profile'),
        ),
    ]
