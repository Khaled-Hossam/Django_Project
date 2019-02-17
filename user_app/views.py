from django.shortcuts import render
from user_app.forms import UserForm, UserUpdateInfoForm
from user_app.models import UserProfileInfo

# login imports
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "user_app/index.html")

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    registerd = False
    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserUpdateInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()

            registerd = True
        # else:
            # raise user_form.errors
    
    else:
        user_form = UserForm()
        profile_form = UserUpdateInfoForm()

    return render(request,'user_app/register.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registerd
    })

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
        
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password =  request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return render(request,'user_app/login.html',context={"inactive":True,})

        else:
            return render(request,'user_app/login.html',context={"invalid":True,"username":username,})

    else:
        return render(request,'user_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# @login_required
# def special(request):
#     return HttpResponse("Logged in!")

@login_required
def user_profile(request):
    user_info = UserProfileInfo.objects.get(user=request.user)
    return render(request,'user_app/user_profile.html',{"user":request.user,"user_info":user_info})