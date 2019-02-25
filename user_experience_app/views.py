from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Subquery
from django.views.generic import CreateView
from .forms import *
from user_app.models import UserProfileInfo
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from countries.models import *
from django.shortcuts import redirect


def show_city_articles(request,city_id):
    comments=Comment.objects.select_related().values('post__id','post__title','post__post_content','comment_content','post__user_id','user__user_username','user__profile_picture').filter(post__city_id=city_id).order_by('-post__id')
    for i in range(len(comments)):
            for j in range(i+1, len(comments)):
                if comments[i]['post__id'] == comments[j]['post__id']:
                        comments[j]['post__title']=""
                        comments[j]['post__post_content']=""     

    
    posts_without_comments=Post.objects.values('id','title','post_content').exclude(id__in=Comment.objects.values('post__id')).filter(city_id=city_id)
    countries=Country.objects.all()
    posts_data={'article_data':comments,'posts':posts_without_comments,'countries':countries}
    
    return render(request,"user_experience_app/city_page.html",posts_data)


def add_comment(request,city_id,user_id,post_id):
        countries = Country.objects.all()
        if request.method=='POST':
                form=CommentForm(request.POST)
                if form.is_valid(): 
                        obj=form.save(commit=False)
                        obj.post=Post.objects.get(id=post_id)
                        obj.user=UserProfileInfo.objects.get(id=request.user.id)
                        obj.save()
                
                url = '/user_experience_app/city/'+ city_id
                return HttpResponseRedirect(url)
        else:
                form=CommentForm()
                context={'st_form':form}
                return render(request,'user_experience_app/add_comment.html',{'form':form,'countries':countries})
        

     


def add_post(request,city_id,user_id):
        countries = Country.objects.all()
        
        if request.method=='POST':
                form=PostForm(request.POST)
                if form.is_valid():
                        obj=form.save(commit=False)
                        obj.city=City.objects.get(id=city_id)
                        obj.user=UserProfileInfo.objects.get(id=request.user.id)
                        form.save()
                url = '/user_experience_app/city/'+ city_id
                return HttpResponseRedirect(url)
        else:
                form=PostForm()
                context={'st_form',form}
                return render(request,'user_experience_app/add_post.html',{'form':form,'countries':countries})



