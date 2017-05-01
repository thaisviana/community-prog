from django.contrib import admin
from django.db import models


class PDFContent(models.Model):
    name = models.CharField('nome', max_length=255)
    file = models.FileField()
    category = models.OneToOneField('Category', default=1)
    description = models.CharField('descrição', max_length=255)

    @classmethod
    def register_admin(cls):
        """Registers this class's main admin."""
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'description')

