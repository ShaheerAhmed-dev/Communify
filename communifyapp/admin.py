from django.contrib import admin
from .models import CustomUser, Post, Comment, Profile, Like, Share

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Share)