"""django_project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# we need to import the views of this app just to display the home page
from countries import views
# from user_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$',views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^countries/', include('countries.urls')), 
    # url(r'^', views.index),
    url(r'^user_app/',include('user_app.urls')),
    url(r'^user_experience_app/',include('user_experience_app.urls')),
    # url(r'^logout/$',views.user_logout,name='logout')
   
    url(r'^book_hotel/',include('hotel.urls')), ### user came to book a room in a hotel
    url(r'^book_car/', include('car.urls')), ### user came to book a car 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 