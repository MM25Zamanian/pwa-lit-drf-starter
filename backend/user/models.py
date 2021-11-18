from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from utils import GeneralModel


class User(AbstractUser, GeneralModel):
    email = models.EmailField(
        _("email address"),
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',
                message=_('This email is invalid')
            )
        ],
    )
    biography = models.TextField(
        max_length=1000,
        verbose_name=_("biography"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
