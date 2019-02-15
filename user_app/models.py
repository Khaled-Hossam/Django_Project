from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# in User model there is an attribute called is_superuser and is_staff
# both are boolean values 
# is_superuser: Designates that this user has all permissions without explicitly assigning them.
# is_staff:  Designates whether this user can access the admin site.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    # TODO: add gender

    def __str__(self):
        return self.user.get_full_name()