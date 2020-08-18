
from django.utils.translation import ugettext_lazy as _
from generic_chooser.widgets import AdminChooser
from . import SchoolProfile
from wagtail.core import hooks
from generic_chooser.views import ModelChooserViewSet


class SchoolChooserViewSet(ModelChooserViewSet):

    icon = 'user'
    model = SchoolProfile
    page_title = _("Choose A School")
    per_page = 20
    order_by = 'school_name'
    # fields = ['school_name', 'primary_contact']



@hooks.register('register_admin_viewset')
def register_lexis_chooser_viewset():
    return SchoolChooserViewSet('school_chooser', url_prefix='school-chooser')


class SchoolChooser(AdminChooser):
    choose_one_text = _('Choose a School')
    choose_another_text = _('Choose another School')
    link_to_chosen_text = _('Edit this School')
    model = SchoolProfile
    choose_modal_url_name = 'school_chooser:choose'



