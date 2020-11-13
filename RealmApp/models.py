from django.db import models
from django.contrib.auth.models import User

status = (
    (0, 'Draft'),
    (1, 'Publish'),
)


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    slug = models.SlugField(max_length= 200, unique= True)
    content = models.TextField()
    picture = models.ImageField(upload_to='media/images')
    created_on = models.DateTimeField(auto_now= True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=status, default=1)
