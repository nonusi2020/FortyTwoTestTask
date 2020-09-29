from apps.fortytwoapps import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, dispatch_uid="my_unique_identifier")
def models_log_post_save(sender, instance, created, raw, **kwargs):
    # print("kwwwad:",kwargs)
    if sender.__name__ in ['ModelsLog', 'Migration', 'Session', 'ContentType']:
        return
    action = 'created' if created else 'updated'
    models.ModelsLog.objects.create(
        appname=instance._meta.app_label,
        objectname=instance._meta.object_name, action=action
    )


@receiver(post_delete, dispatch_uid="my_unique_identifier")
def models_log_post_delete(sender, instance, **kwargs):
    if sender == models.ModelsLog:
        return
    action = 'deleted'
    models.ModelsLog.objects.create(
        appname=instance._meta.app_label,
        objectname=instance._meta.object_name, action=action
    )
