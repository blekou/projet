from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Client
from django.contrib.auth.models import Group

def profil_client(sender, instance, created, **kwargs):

    if created:
        group  = Group.objects.get(name="client")
        instance.groups.add(group)

        Client.objects.create(
            user = instance,
            name = instance.username,
        )
post_save.connect(profil_client,sender=User )



