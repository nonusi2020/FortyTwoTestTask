from django.db.models.signals import post_save, post_delete
from apps.fortytwoapps.models import ModelsLog
from django.dispatch import receiver


@receiver(post_save, dispatch_uid="my_unique_identifier")
def models_log_post_save(sender, instance, created, raw, **kwargs):
    if raw or sender == ModelsLog:
        return
    action = 'created' if created else 'updated'
    ModelsLog.objects.create(appname=instance._meta.app_label, objectname=instance._meta.object_name, action=action)


@receiver(post_delete, dispatch_uid="my_unique_identifier")
def object_log_post_delete(sender, instance, **kwargs):
    if sender == ModelsLog:
        return
    action = 'deleted'
    ModelsLog.objects.create(appname=instance._meta.app_label, objectname=instance._meta.object_name, action=action)
