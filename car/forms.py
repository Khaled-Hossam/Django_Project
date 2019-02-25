from django import forms
from .models import CarReservationRequest



# form class
class reservationForm(forms.ModelForm):

    class Meta:
        model = CarReservationRequest
        #user_id included in our fields
        #,'pick_up_point','destination'
        #fields = ('car_requested',)
        fields = ('pick_up_point', 'destination' ,'pick_up_date','Drop_off_date','pick_up_time','Drop_off_time')

        def __init__(self, *args, **kwargs):
            super(reservationForm, self).__init__(*args, **kwargs)
           # self.fields['car_requested'].queryset = Car.objects.filter(city_id = '1')
            #self.fields['destination'].queryset = Sight.objects.filter()
            #self.fields['pick_up_point'].queryset = Sight.objects.filter()
	    ## number 1 in last line is merely a test.