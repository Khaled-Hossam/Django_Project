from django.shortcuts import render
from .forms import reservationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from user_app.models import UserProfileInfo
from django.contrib.auth import authenticate # added by Mahydit to authenticate
from django.core.urlresolvers import reverse # added by Mahydit to authenticate

# Create your views here.


def reservation(request, city_id):
        if request.user.is_authenticated: # added by Mahydit to authenticate
                form = reservationForm()
                if request.method == "POST":
                        form = reservationForm(request.POST)
                        if form.is_valid():
                                obj=form.save(commit=False)
                                
                                obj.user= request.user
                                obj.save()
                              #  return HttpResponse("<div class='alert alert-success '>Booking Done </div>")
                                return redirect('/countries/cities/'+ city_id)
                return render(request, 'car.html', {'form':form})

                #form = form.save(commit=False)
                #form.save()

        else: # added by Mahydit to authenticate
                return HttpResponseRedirect(reverse("user_app:user_login"))    # added by Mahydit to authenticate 
