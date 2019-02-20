from django.db import models
from datetime import date
from datetime import datetime
import datetime
# from user_app import UserProfileInfo
from django.contrib.auth.models import User
#from app.models import cities ##cities is the name of the class in khalid's app.models
##if it is different(name) it's fine just change the name in your code to validate with khalid


# table linking user to hotels
class CarReservationRequest(models.Model):

    car_requested= models.AutoField(primary_key=True)
    #user_id = models.ForeignKey(User)
    user_id = models.ForeignKey(User)
    pick_up_date = models.DateField(default=datetime.date.today)
    Drop_off_date = models.DateField(default=datetime.date.today)
    pick_up_time = models.TimeField(default='00:00')
    Drop_off_time = models.TimeField(default='00:00')
    # pick_up_point = models.ForeignKey('city.Location',related_name='pick_up_point')
    #destination = models.ForeignKey('city.Location',related_name='destination')

    #def __str__(self):
        #return self.pick_up_point
    #def __str__(self):
        #return self.destination   
      