from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    profile = UserProfile.objects.create(user=instance)
    print(profile)
