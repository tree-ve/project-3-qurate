from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
# ? class Profile(models.Model):
# ?     user = models.OneToOneField(User, on_delete=models.CASCADE)
# ?     created_at = models.DateTimeField(auto_now_add=True)


# class Follow(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     following_user = models.ForeignKey(User, related_name="following", on_delete=models.DO_NOTHING)
#     follower_user = models.ForeignKey(User, related_name="followers", on_delete=models.DO_NOTHING)
#     date_followed = models.DateTimeField(auto_now_add=True, db_index=True)
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['following_user','follower_user'],  name="unique_followers")
#         ]
#         ordering = ["-date_followed"]
#     def __str__(self):
#         f"{self.user_id} follows {self.following_user_id}"


# class Tag(models.Model):
#     label = models.CharField(max_length=20)


class Post(models.Model):
    url = models.CharField(max_length=200)
    # url = models.ImageField()
    # ? Changed this to reference User rather than Profile, as it allowed for the profile model to consolidate more information
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    description = models.CharField(max_length=300, blank=True)
    # tags = models.ManyToManyField(Tag)
    tags = models.CharField(max_length=30, blank=True)
    likes = models.IntegerField(default=0)
    #likes = model.ManyToManyField(User, related_name = 'qurate_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('user_feed')

# class LikePost(models.Model):
#     post = models.ForeignKey(Post, )
#     username = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.username

class Comment(models.Model):
    # ? Changed this to reference User rather than Profile, as it allowed for the profile model to consolidate more information
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Sub_Comment(Comment):
#     parent = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)

# class User_likes(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     posts = models.ManyToManyField(Post, related_name="posts_liked")
#     comments = models.ManyToManyField(Comment, related_name="comments_liked")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post_likes = models.ManyToManyField(Post, related_name="posts_liked", blank=True)
    comment_likes = models.ManyToManyField(Comment, related_name="comments_liked", blank=True)
    following_list = models.ManyToManyField('self', through='Follow_List', blank=True)
    # ? Follower list might need to be removed down the line, I haven't seen it in any profile examples I've seen
    follower_list = models.ManyToManyField('self', blank=True)
    def __str__(self):
        return f'{self.user} user.id: ({self.user_id}) profile id: ({self.id})'

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Follow_List(models.Model):
    following = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True, db_index=True)