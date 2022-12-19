# create signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile 

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    print("Profile signal triggereed", sender)
    print("UserName: ", instance)
    print("Kwargs: ", kwargs)
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, 
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        # send emails template form django docs
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
        

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    # one-one relationship resulting to access user with profile_model too
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.name
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    print(user, "got deleted deleted")
    user.delete()

# trigering an update(model B) after updating model A

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)