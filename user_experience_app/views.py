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
    


# def index(request):
#     return HttpResponse("<h1>Hello Proooooject Django</h1>")

# def first(request):
#     return render(request,"first.html")

# ///////////////////////////////////////////////////////////////////////////////////////////
    

# def show_city_articles(request,city_id):
#     comments=Comment.objects.select_related().values('post__id','post__title','post__post_content','comment_content','post__user_id','user__user_username','user__profile_picture').filter(post__city_id=city_id).order_by('-post__id')
#     for i in range(len(comments)):
#             for j in range(i+1, len(comments)):
#                 if comments[i]['post__id'] == comments[j]['post__id']:
#                         comments[j]['post__title']=""
#                         comments[j]['post__post_content']=""               
    
#     posts_data={'article_data':comments}
#     return render(request,"user_experience_app/city_page.html",posts_data)

def show_city_articles(request,city_id):
    comments=Comment.objects.select_related().values('post__id','post__title','post__post_content','comment_content','post__user_id','user__user_username','user__profile_picture').filter(post__city_id=city_id).order_by('-post__id')
    for i in range(len(comments)):
            for j in range(i+1, len(comments)):
                if comments[i]['post__id'] == comments[j]['post__id']:
                        comments[j]['post__title']=""
                        comments[j]['post__post_content']=""     

    
    posts_without_comments=Post.objects.values('id','title','post_content').exclude(id__in=Comment.objects.values('post__id')).filter(city_id=city_id)
    countries=Country.objects.all()
    posts_data={'article_data':comments,'posts':posts_without_comments,'country':countries}
    
#     posts_data={'article_data':comments}
    return render(request,"user_experience_app/city_page.html",posts_data)




    


def add_comment(request,city_id,user_id,post_id):
        if request.user.is_authenticated:
                if request.method=='POST':
                        form=CommentForm(request.POST)
                        if form.is_valid(): 
                                obj=form.save(commit=False)
                                obj.post=Post.objects.get(id=post_id)
                                obj.user=UserProfileInfo.objects.get(id=request.user.id)
                                obj.save()

                        return HttpResponseRedirect('/user_experience_app/city/1')
                else:
                        form=CommentForm()
                        context={'st_form',form}
                        return render(request,'user_experience_app/add_comment.html',{'form':form})
        
        else:
                return HttpResponseRedirect(reverse("user_app:user_login"))

     


def add_post(request,city_id,user_id):
        if request.user.is_authenticated:

                if request.method=='POST':
                        form=PostForm(request.POST)
                        if form.is_valid():
                                obj=form.save(commit=False)
                                obj.city=City.objects.get(id=city_id)
                                obj.user=UserProfileInfo.objects.get(id=request.user.id)
                                form.save()

                        return HttpResponseRedirect('/user_experience_app/city/1')
                else:
                        form=PostForm()
                        context={'st_form',form}
                        return render(request,'user_experience_app/add_post.html',{'form':form})

        else:
                return HttpResponseRedirect(reverse("user_app:user_login"))



  #/////////////////////////////////////////////////////// 


# //////////////////////////////////////////////////////////////////////////////////////////////////////

# def add_comment(request,city_id,user_id,post_id):
#         if request.method=='POST':
#                 form=CommentForm(request.POST)
#                 if form.is_valid():
#                         commnet=form.save(commit=false)
#                         commnet.post=post__id
#                         commnet.user=user_id
#                         comment.save()
#                         #commnet.user=request.user
#                         return HttpResponseRedirect('/user_experience_app/city/1')
#         else:
#                 form=CommentForm()
#                 context={'st_form',form}
#                 return render(request,{'form':form})


# //////////////////////////////////////////////////////////////////


# def show_city_articles(request,city_id):
#     articles=Post.objects.filter(city_id=city_id)
#     comments=Comment.objects.filter(post_id__in=Subquery(articles.values('id')))
#     posts_data={'article_data':comments}
#     return render(request,"city_page.html",posts_data)


# def show_city_articles(request,city_id):
#     articles=City.objects.select_related('posts','comments').filter(id=city_id)
#     posts_data={'article_data':articles}
#     return render(request,"city_page.html",posts_data)

# pubs = publication.objects.select_related('country', 'country_state', 'city')

# def show_all_experiences(request, news_id=1):
#     news = Article.objects.get(id=article_id)
#     comments = Comment.objects.filter(comments_news_id=article_id)
#     return render(request, 'page.html', {'news': news, 'comments': comments})

