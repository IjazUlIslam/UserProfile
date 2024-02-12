from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def custom_user_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.first_name and instance.last_name:
            instance.full_name = instance.first_name + ' ' + instance.last_name
        instance.login_date = datetime.datetime.now()
        instance.save()


post_save.connect(custom_user_post_save, sender=CustomUser)
