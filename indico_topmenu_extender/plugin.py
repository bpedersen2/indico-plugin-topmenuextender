from indico.core import signals
from indico.core.plugins import IndicoPlugin
from indico.util.i18n import _
from indico.web.forms.base import IndicoForm
from indico.web.forms.fields import MultipleItemsField
from indico.web.menu import TopMenuItem

MENU_FIELDS= [{'id': 'menu_key', 'caption': _("Menu key"), 'required': True},
              {'id': 'menu_title', 'caption': _("Menu title"), 'required': True},
              {'id': 'menu_url', 'caption': _("Menu url"), 'required': True},
              {'id': 'menu_weight', 'caption': _("Menu weight"), 'required': False},
              ]

class SettingsForm(IndicoForm):
    top_menu_entries = MultipleItemsField(_('Top Menu entries'), fields=MENU_FIELDS, unique_field='menu_key')

class TopMenuExtenderPlugin(IndicoPlugin):
    """Custom Top Menu Links

    Add a new top menu links.
    """

    configurable = True
    settings_form = SettingsForm
    default_settings = {
            'top_menu_entries': [],
    }

    def init(self):
        super().init()
        self.connect(signals.menu.items, self._extend_top_menu, sender='top-menu')

    def _extend_top_menu(self, sender, **kwargs):
        for entry in  self.settings.get('top_menu_entries'):
            yield TopMenuItem(entry['menu_key'], entry['menu_title'], entry['menu_url'], weight=entry.get('menu_weight', 95))
