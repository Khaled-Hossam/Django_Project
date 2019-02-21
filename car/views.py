from django.shortcuts import render
from .forms import reservationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from user_app.models import UserProfileInfo
# Create your views here.


def reservation(request):
    form = reservationForm()
    if request.method == "POST":
        form = reservationForm(request.POST)
        if form.is_valid():
                obj=form.save(commit=False)
                obj.user=UserProfileInfo.objects.get(id=1)
                obj.save()
                return HttpResponse("<div class='alert alert-success '>Booking Done </div>")
    return render(request, 'car.html', {'form':form})

    #form = form.save(commit=False)
    #form.save()