from django.shortcuts import render
from user_app.forms import *
from user_app.models import UserProfileInfo
from countries.models import Country

# login imports
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# def index(request):
#     return render(request, "countries/index.html")

def register(request):
    countries = Country.objects.all()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('countries:index'))

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserUpdateInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.user_username = user.username

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()
            return HttpResponseRedirect(reverse('user_app:user_login'))

    
    else:
        user_form = UserForm()
        profile_form = UserUpdateInfoForm()

    return render(request,'accounts/register.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'countries':countries,
    })

def user_login(request):
    countries = Country.objects.all()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('countries:index'))
        
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password =  request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('countries:index'))

            else:
                return render(request,'accounts/login.html',context={"inactive":True,'countries':countries,})

        else:
            return render(request,'accounts/login.html',context={"invalid":True,"username":username,'countries':countries,})

    else:
        return render(request,'accounts/login.html',context={'countries':countries,})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('countries:index'))

@login_required
def user_profile(request):
    countries = Country.objects.all()
    try:
        user_info = UserProfileInfo.objects.get(user=request.user)
    except UserProfileInfo.DoesNotExist:
       user_info = None

    return render(request,'accounts/user_profile.html',{"user":request.user,"user_info":user_info,'countries':countries,})

@login_required
def user_update_profile(request):
    countries = Country.objects.all()
    try:
        user_info = UserProfileInfo.objects.get(user=request.user)
    except UserProfileInfo.DoesNotExist:
       user_info = None

    if request.method =='POST':
        form = UserProfileUpdate(request.POST, instance= request.user)
        pic_form = UserProfileInfoUpdate(request.POST)
        if form.is_valid():

            if pic_form.is_valid:
                if 'profile_picture' in request.FILES:
                    updated_pic = UserProfileInfo.objects.get(pk=request.user.id)
                    updated_pic.profile_picture = request.FILES['profile_picture']
                    updated_pic.save()
                # UserProfileInfo.objects.filter(pk=request.user.id).update(profile_picture = updated_pic.profile_picture )
            else:
                context = {"user_form":form,"user_pic":pic_form,"user_info":user_info,'countries':countries,}
                return render(request,'accounts/user_update_profile.html',context)  

            form.save()
            return HttpResponseRedirect(reverse('user_app:user_profile'))

        else:
            context = {"user_form":form,"user_pic":pic_form,"user_info":user_info,'countries':countries,}
            return render(request,'accounts/user_update_profile.html',context)

    else:
        pic_form = UserProfileInfoUpdate(request.POST)
        form = UserProfileUpdate(instance = request.user)
        context = {'user_form':form,"user_pic":pic_form,"user_info":user_info,'countries':countries,}
        return render(request,'accounts/user_update_profile.html',context)