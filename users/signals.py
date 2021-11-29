from types import BuiltinMethodType
from django.db.models.signals import post_save,post_delete
from django.dispatch.dispatcher import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.conf import settings
from django.core.mail import message, send_mail

#@receiver(post_save,sender=user)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username= user.username,
            email = user.email,
            name = user.first_name,
        )
        subject = 'Welcome to DevSearch'
        message = 'Hi there!,\n\nMy name is Rahul Jangir,I am the Co-founder and CEO of devsearch. I wanted to personally welcome to you to devsearch on behalf of our entire team.\nYou are already one step closer to improving your customer support performance,\n \nIf you have any questions, just let me know. See you inside  devsearch. \n ... \nBest regards,\nRahul Jangir\nCo-founder and CEO of devsearch '

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created ==False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


#@receiver(post_delete,sender = user)
def deleteUser(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(createProfile,sender = User)
post_save.connect(updateUser,sender = Profile)
post_delete.connect(deleteUser,sender = Profile)