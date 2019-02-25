"""python_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from user_experience_app import views


urlpatterns = [
    url(r'^city/(?P<city_id>[0-9]+)/$',views.show_city_articles, name="city_posts"),
    url(r'^city/(?P<city_id>[0-9]+)/(?P<post_id>[0-9]+)/(?P<user_id>[0-9]+)/$',views.add_comment),
    url(r'^city/(?P<city_id>[0-9]+)/add_post/(?P<user_id>[0-9]+)/$',views.add_post),

]
