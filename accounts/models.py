from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from django.dispatch import receiver

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):

    INTERESTS_CHOICES = (
           ('Project Manager','Project Manager'),
           ('Project Scheduler','Project Scheduler'),
           ('Information Technology Analyst','Information Technology Analyst'),
           ('Information Technology Engineer','Information Technology Engineer'),
           ('Information Technology Programmer','Information Technology Programmer'),
           ('Information Technology Architect','Information Technology Architect')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    resume = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    interests = MultiSelectField(choices= INTERESTS_CHOICES, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()    