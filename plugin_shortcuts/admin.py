from django.contrib import admin
from django.utils.translation import ugettext as _

from models import ShortcutsPluginModel, ShortcutModel


class ShortcutAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_creacion'
    list_display = ('fecha_creacion','titulo', 'publicado')
    list_display_links = ('titulo',)
    list_filter = ('titulo', 'publicado')

admin.site.register(ShortcutModel, ShortcutAdmin)
