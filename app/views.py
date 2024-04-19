import os

from django.conf import settings
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Counter, Post

def home(request):
    post = Post.objects.first()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Delete previous images if any
            clear_media()
            Post.objects.all().delete()
            # Save the new image
            form.save()
            return redirect('home')
        else:
            return render(request, "app/home.html", {"post": post, "form": form})
    else:
        form = PostForm()
    
    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()
    
    counter.count += 1
    counter.save()
    context = {
        "count": counter.count,
        "post": post,
        "form": form
    }
    return render(request, "app/home.html", context)

def clear_media():
    media_folder = settings.MEDIA_ROOT
    if os.path.exists(media_folder):
        # Delete all files in the folder
        for filename in os.listdir(media_folder):
            file_path = os.path.join(media_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")