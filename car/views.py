from django.shortcuts import render
from .forms import reservationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.


def reservation(request):
    form = reservationForm()
    if request.method == "POST":
        form = reservationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponse("<div class='alert alert-success '>Booking Done </div>")
    return render(request, 'car.html', {'form':form})