from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from cms.models import Page
from cms.models.fields import PlaceholderField



class ShortcutsMosaicModel(CMSPlugin):
    columnas = models.IntegerField(null=False,blank=False, default=1)


class ShortcutsPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        ('plugin_shortcuts/barra.html', 'Barra'),
        ('plugin_shortcuts/lista.html', 'Lista'),
    )
    numero = models.IntegerField(null=False,blank=False, default=1)
    plantilla = models.CharField('Template', max_length=255,
                                choices = PLUGIN_TEMPLATES)



class ShortcutPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        ('plugin_shortcuts/shortcut.html', 'Linea'),
        ('plugin_shortcuts/item.html', 'Mosaico'),
    )
    fecha_creacion = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length="100", blank=True, default='')
    imagen = FilerImageField(blank=True, null=True)
    publicado = models.BooleanField(default=True)
    descripcion = models.TextField(max_length="350", default='', blank=True, null=True)
    mostrar_descripcion = models.BooleanField(default=True)
    pagina = models.ForeignKey(Page, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True, null=True)
    plantilla = models.CharField('Template', max_length=255, choices = PLUGIN_TEMPLATES, default=PLUGIN_TEMPLATES[0][0])
    mostrar_boton_ver_mas = models.BooleanField(default=False)    

    def __unicode__(self):
        return self.titulo


class ShortcutModel(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length="100", blank=True, default='')
    imagen = FilerImageField(blank=False)
    publicado = models.BooleanField(default=True)
    pagina = models.ForeignKey(Page, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Shortcut"
        verbose_name_plural = "Shortcuts"
