import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Group,Permission
from django.contrib.contenttypes.models import ContentType
from mainapp.models import CustomUser


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        ct = ContentType.objects.get_for_model(CustomUser)
        group_gerant, created = Group.objects.get_or_create(name="gerant_new")
        if (created):
            gerant_permission = Permission.objects.create(codename='gerant_default_new',
                                    name='Gerant default new',
                                    content_type=ct)
            group_gerant.permissions.add(gerant_permission)
            group_gerant.save()
        
        
        group_agent, created = Group.objects.get_or_create(name="agent_new")
        if (created):
            gerant_permission = Permission.objects.create(codename='agent_default_new',
                                    name='Agent default new ',
                                    content_type=ct)
            group_agent.permissions.add(gerant_permission)
            group_agent.save()

       
       
    def handle(self, *args, **options):
         pass