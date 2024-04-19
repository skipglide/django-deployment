from django.contrib import admin

from .models import Counter, Post

admin.site.register(Counter)
admin.site.register(Post)