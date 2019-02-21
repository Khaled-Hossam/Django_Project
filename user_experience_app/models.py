from django.db import models
from user_app.models import UserProfileInfo
from countries.models import *


# # Create your models here.
# class Country(models.Model):
#     country_name=models.CharField(max_length=200)
#     description=models.CharField(max_length=1000)
#     img=models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.country_name


# class City(models.Model):
#     city_name=models.CharField(max_length=200)
#     description=models.CharField(max_length=2000)
#     rate=models.IntegerField()
#     country=models.ForeignKey(Country,related_name='cities')#FK from Country class

#     def __str__(self):
#         return self.city_name


# class User(models.Model):
#     user_name=models.CharField(max_length=200)
#     email = models.EmailField() 
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     img=models.CharField(max_length=50)

#     def __str__(self):
#         return self.user_name


class Post(models.Model):
    title=models.CharField(max_length=100)
    post_content=models.TextField()
    user=models.ForeignKey(UserProfileInfo ,related_name='posts')
    city=models.ForeignKey(City,related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_content=models.TextField()
    user=models.ForeignKey(UserProfileInfo,related_name='comments')
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment_content









    
    
