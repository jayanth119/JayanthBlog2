from django.db import models
from django.utils.html import format_html


from django.urls import reverse 
# Create your models here.

# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title

# class Ipmodel(models.Model):
#     ip = models.CharField(max_length=100) 
#     def __str__(self) -> str:
#         return self.ip 

# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='post/')

    # likes = models.ManyToManyField(Ipmodel , related_name='post_likes' , blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'url': self.url})
    # def total_likes(self):
    #     return self.likes.count 
    