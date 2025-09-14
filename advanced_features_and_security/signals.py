# advanced_features_and_security/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

@receiver(post_migrate)
def create_groups_and_assign_permissions(sender, **kwargs):
    """
    After migrations run, create groups and attach permissions.
    """
    if sender.name != "advanced_features_and_security":
        return

    # Get the Article model
    Article = apps.get_model('advanced_features_and_security', 'Article')
    ct = ContentType.objects.get_for_model(Article)

    # Define groups and their permissions
    groups_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perm_codenames in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for codename in perm_codenames:
            try:
                perm = Permission.objects.get(codename=codename, content_type=ct)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                pass
