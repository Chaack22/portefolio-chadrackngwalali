from django.db.models.signals import post_save
from .models import Message
from django.dispatch import receiver

@receiver(post_save, sender = Message)
def notification(sender, instance,created,**kwargs):
    if created:
        print(f"\n\n Nouveau message de la par de {instance.nom}, \n\n")
   