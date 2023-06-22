import uuid
import boto3
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from main_app.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Post, Comment
from .forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ! PAGES --------------------------
# @login_required
def user_feed(request):

    return render(request, 'qurate/feed.html', {
        'title': 'Your Feed'
    })

def explore(request):
        posts = Post.objects.all()
        return render(request, 'qurate/explore.html', {
        'posts': posts,
        'title': 'Explore'
    })


def inspo(request):
        return render(request, 'qurate/inspiration.html', {
            'title': 'Inspiration'
    })

# @login_required
def posts_detail(request, posts_id):

    return render(request, 'posts/detail.html', {

    })

# ! POSTS ------------------

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'price', 'description', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        photo_file = self.request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                post = form.save(commit=False)
                post.url = url
                post.save()
            except Exception as e:
                print('An error occurred uploading file to S3')
        return super().form_valid(form)
        




class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'price', 'description', 'tags']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts'

# ! COMMENTS ---------------------

def add_comment(request, post_id):
 return render(request, 'posts/add_comment.html', {

    })


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment


# ! TAGS ----------------------
def tags_index(request, tags):
    posts = Post.objects.filter(tags=tags)
    return render(request, 'qurate/tags.html', {
        'title': '#' + tags,
        'posts': posts
    })



# ! USERS --------------------

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def users_detail(request, user_id):
    profile = Profile.objects.get(id=user_id)
    user_form = UserCreationForm()
    return render(request, 'users/detail.html', {
        'profile': profile, 'user_form': user_form,
    })

