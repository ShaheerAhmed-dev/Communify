
from django.contrib.auth.models import AbstractUser, Permission
from PIL import Image
from django.db import models
from datetime import date



# Create your models here.

class UserModel(AbstractUser):
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
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
    
class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.models.DateField(default=date.today)
    type = models.ForeignKey('PostType', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.id}"
    
class PostType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_name
    
