from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False, blank=False)

def __str__(self):
        return "{0} - {1}".format(self.user.username, self.designation)


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

