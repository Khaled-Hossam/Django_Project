from django.db import models
from django.contrib.auth.models import User

def pics_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/profile_pics/<user.id>
    return 'profile_pics/{}'.format(instance.user.id)

# in User model there is an attribute called is_superuser and is_staff
# both are boolean values 
# is_superuser: Designates that this user has all permissions without explicitly assigning them.
# is_staff:  Designates whether this user can access the admin site.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to=pics_directory_path,blank=True)
    user_username = models.CharField(max_length=40,default='null')
    # TODO: add gender

    def __str__(self):
        return self.user.get_full_name()

    def clean_username(self):
        return self.username.lower()

    def clean_email(self):
        return self.email.lower()
