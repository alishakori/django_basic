from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, )
    avatar=models.FileField(upload_to="files/user_avatar/", blank=False, null=False, validators=[validate_file_extension])
    discription=models.CharField(max_length=512, null=False, blank=False)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=155, blank=False, null=False)
    cover=models.FileField(upload_to='files/category_cover/',blank=False, null=False, validators=[validate_file_extension])
    def __str__(self):
        return self.title

class Artical(models.Model):
    title=models.CharField(max_length=150, blank=False, null=False)
    cover=models.FileField(upload_to='files/artical_conver/', blank=False, null=False,validators=[validate_file_extension])
    content=RichTextField(config_name='awesome_ckeditor')
    Created_at=models.DateTimeField(default=datetime.now,blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    #promote = models.BooleanField(default=False)
    



 


