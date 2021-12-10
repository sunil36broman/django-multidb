from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Blog(model.Model):
    title=models.CharField(_("title"), max_length=50)
    body=models.CharField(_("body"), max_length=50)

    def __str__(self):
        return self.title