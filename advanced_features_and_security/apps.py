from django.apps import AppConfig

class AdvancedFeaturesAndSecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advanced_features_and_security'

    def ready(self):
        # import signals to ensure they are registered
        import advanced_features_and_security.signals  # noqa: F401

