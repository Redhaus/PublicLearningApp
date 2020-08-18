
# model admin chooser panels
from django.utils.translation import ugettext_lazy as _
from generic_chooser.widgets import AdminChooser
from . import Lexis
from wagtail.core import hooks
from generic_chooser.views import ModelChooserViewSet


class LexisChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = Lexis
    page_title = _("Choose A Lexis Term")
    per_page = 20
    order_by = 'term'
    # fields = ['term', 'part_of_speech']


@hooks.register('register_admin_viewset')
def register_lexis_chooser_viewset():
    return LexisChooserViewSet('lexis_chooser', url_prefix='lexis-chooser')


class LexisChooser(AdminChooser):
    choose_one_text = _('Choose a Lexis')
    choose_another_text = _('Choose another Lexis')
    link_to_chosen_text = _('Edit this Lexis')
    model = Lexis
    choose_modal_url_name = 'lexis_chooser:choose'


