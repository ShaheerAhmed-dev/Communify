import os

from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db import models

from datetime import date
# from django.contrib.auth.models import User



# Create your models here.

#         return user
class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # your save logic here
        super().save(*args, **kwargs)
        return self
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return os.path.join('profile_pics', filename)
class Profile(models.Model):
    about_me = models.TextField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default = 'profile_pics/default.jpg', upload_to = content_file_name)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    
class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length= 5000, blank=True, null=True)
    image = models.ImageField(upload_to='thought_images/', blank=True, null=True)
    private = models.BooleanField(default=False)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # date = models.DateField(default=date.auto_now)
    type = models.CharField(max_length=255, choices=[('social', 'Social'), ('political', 'Political'), ('Economic', 'Economic'), ('other', 'Other')])

    def __str__(self):
        return f"Post {self.id}"


    class Meta:
        ordering = ('-date',)


    
# class PostType(models.Model):
#     type_id = models.AutoField(primary_key=True)
#     type_name = models.CharField(max_length=255, choices=[('social', 'Social'), ('political', 'Political'), ('Economic', 'Economic'), ('other', 'Other')])
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.type_name
class Comment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    # def __str__(self):
    #     return 'Comment by {}'.format(self.user)
