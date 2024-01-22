
from django.contrib.auth.models import AbstractUser, Permission, BaseUserManager
from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#         return user
class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    profile_id = models.OneToOneField(Profile, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    text = models.TextField(max_length= 5000, blank=True, null=True)
    image = models.ImageField(upload_to='thought_images/', blank=True, null=True)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='post_likes', blank=True)



    def __str__(self):
        return f"Post {self.id}"
    
class PostType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_name
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on Post {self.post.id}'