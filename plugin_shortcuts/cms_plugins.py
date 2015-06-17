from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import ShortcutsPluginModel,ShortcutPluginModel, ShortcutModel
from models import ShortcutsMosaicModel



class ShortcutsMosaicPlugin(CMSPluginBase):
    model = ShortcutsMosaicModel
    name = _("Shortcut Mosaic Plugin")
    render_template =  "plugin_shortcuts/mosaic.html"
    def render(self, context, instance, placeholder):
        context['columns'] = instance.columnas
        return context


class ShortcutPlugin(CMSPluginBase):
    model = ShortcutPluginModel
    name = _("Shortcut Plugin")
    render_template = ShortcutPluginModel.PLUGIN_TEMPLATES[0][0]

    def render(self, context, instance, placeholder):
        if instance and instance.plantilla:
            self.render_template = instance.plantilla
        context['instance'] = instance
        return context


class ShortcutsPlugin(CMSPluginBase):
    model = ShortcutsPluginModel
    name = _("Shortcuts Plugin")
    render_template = ShortcutsPluginModel.PLUGIN_TEMPLATES[0][0]

    def render(self, context, instance, placeholder):
        if instance and instance.plantilla:
            self.render_template = instance.plantilla
        lista = ShortcutModel.objects.filter(publicado=True)
        if instance.numero:
            context['lista'] = lista[:instance.numero]
        else:
            context['lista'] = lista
        return context


plugin_pool.register_plugin(ShortcutsPlugin)
plugin_pool.register_plugin(ShortcutPlugin)
plugin_pool.register_plugin(ShortcutsMosaicPlugin)

