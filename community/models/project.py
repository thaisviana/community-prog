from django.contrib import admin
from django.db import models


class Project(models.Model):
    name = models.CharField('nome', max_length=255)
    description = models.CharField('nome', max_length=255)
    image = models.FileField()
    link = models.URLField(null=True, blank=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def register_admin(cls):
        """Registers this class's main admin."""
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name',)

