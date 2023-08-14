from .models import Profile
from django.db.models.signals import post_save,pre_delete # type of signal
from django.dispatch import receiver


@receiver(post_save, sender = Profile)
def notify_new_profile(sender, instance, **kwargs):
    print(f'New profile! Name: {instance.name} Email: {instance.email}')
    
@receiver(pre_delete, sender=Profile)
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print(f'You are trying to delete an active account! Name: {instance.name}')
        
