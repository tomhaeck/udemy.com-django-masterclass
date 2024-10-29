from django.db.models.signals import post_save
from django.contrib.auth.models import User  # this will be the sender
from django.dispatch import receiver  # this will be the receiver
from users.models import Profile


@receiver(post_save, sender=User)  # this function will be executed if a new User is saved
def build_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()