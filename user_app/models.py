from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def pics_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_pics/{}'.format(instance.user.id)

# in User model there is an attribute called is_superuser and is_staff
# both are boolean values 
# is_superuser: Designates that this user has all permissions without explicitly assigning them.
# is_staff:  Designates whether this user can access the admin site.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to=pics_directory_path,blank=True)
    # TODO: add gender

    def __str__(self):
        return self.user.get_full_name()