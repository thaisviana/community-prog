from django.contrib import admin
from django.db import models


class VideoContent(models.Model):
    name = models.CharField('nome', max_length=255)
    #file = models.FileField()
    url = models.URLField()
    video_id = models.CharField('video_id', max_length=255, blank=True)
    category = models.OneToOneField('Category', default=1)
    description = models.CharField('descrição', max_length=255)

    @classmethod
    def register_admin(cls):
        """Registers this class's main admin."""
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('name', 'description')
    readonly_fields = ('video_id',)

    def save_model(self, request, obj, form, change):
        import re
        m = re.search('(?<=\?v=)[a-zA-z0-9]*', obj.url)
        obj.video_id = m.group(0)
        super(Admin, self).save_model(request, obj, form, change)

