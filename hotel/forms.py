from django import forms
from .models import HotelReservationRequest
from countries.models import Hotel



# form class
class reservationForm(forms.ModelForm):

    class Meta:
        model = HotelReservationRequest
        #user_id included in our fields
        fields = ('hotel_id','from_date', 'to_date', 'no_of_adults',)

        def __init__(self, *args, **kwargs):
            super(reservationForm, self).__init__(*args, **kwargs)
            self.fields['hotel_id'].queryset = Hotel.objects.filter(city_id = 1)
	    ## number 1 in last line is merely a test.
