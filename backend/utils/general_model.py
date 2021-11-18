from django.db import models
from django.utils.translation import gettext as _
import uuid


class GeneralModel(models.Model):
    id = models.UUIDField(
        verbose_name=_('Id'),
        primary_key=True,
        default=uuid.uuid4,
    )
    create_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )

    class Meta:
        abstract = True
