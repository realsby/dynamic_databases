
from logging import getLogger

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from dynamic_databases.models import Database


logger = getLogger('dynamic_databases.receivers')


@receiver([pre_save, pre_delete], sender=Database)
def unregister_database(sender, **kwargs):
    if 'instance' in kwargs:
        kwargs['instance'].unregister()