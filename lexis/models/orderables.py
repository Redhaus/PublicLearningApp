from django.db import models
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from chooser_panels.widgets import EventChooser
from .lexis_chooser import LexisChooser

# # model admin chooser panels
# from django.utils.translation import ugettext_lazy as _
# from generic_chooser.widgets import AdminChooser
# from . import Lexis
# from wagtail.core import hooks
# from generic_chooser.views import ModelChooserViewSet
#
#
# class LexisChooserViewSet(ModelChooserViewSet):
#     icon = 'user'
#     model = Lexis
#     page_title = _("Choose A Lexis Term")
#     per_page = 20
#     order_by = 'term'
#     # fields = ['term', 'part_of_speech']
#
#
# @hooks.register('register_admin_viewset')
# def register_lexis_chooser_viewset():
#     return LexisChooserViewSet('lexis_chooser', url_prefix='lexis-chooser')
#
#
# class LexisChooser(AdminChooser):
#     choose_one_text = _('Choose a Lexis')
#     choose_another_text = _('Choose another Lexis')
#     link_to_chosen_text = _('Edit this Lexis')
#     model = Lexis
#     choose_modal_url_name = 'lexis_chooser:choose'







# make this a category
class IconList(Orderable):
    page = ParentalKey("lexis.Lexis", related_name="icon_list")

    ICON_LIST = (
        ('device', 'device'),
        ('essential', 'essential'),
        ('common', 'common'),
        ('concept', 'concept'),
        ('person', 'person'),
    )

    icons = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=ICON_LIST,
        help_text="Select “device” if the term is a literary or rhetorical device. Select “essential” if the term is necessary knowledge. Select “common” if the term is common knowledge. Select “concept” if the term refers to an idea or historical event. Select “person” if the term refers to a historical or fictional person."
    )

    # add image carousel to panels
    panels = [
        FieldPanel("icons"),
    ]


# Links to multiple collection event_id
class LexisEventCollection(Orderable):
    page = ParentalKey("lexis.Lexis",
                       related_name="related_events"
                       )

    event_link = models.ForeignKey(
        "events.CategoryEventCollection",
        on_delete=models.SET_NULL,
        related_name='event_linked',
        null=True,
        help_text="Select any related events."
    )

    # custom chooser panel
    panels = [
        FieldPanel("event_link", widget=EventChooser),

    ]


# Links to multiple other lexis items
class LexisLink(Orderable):
    page = ParentalKey("lexis.Lexis",
                       related_name="lexis_link"
                       )
    term_link = models.ForeignKey(
        'lexis.Lexis',
        on_delete=models.SET_NULL,
        related_name='term_linked',
        null=True,
        help_text="Select any related lexis terms."
    )

    panels = [
        FieldPanel("term_link", widget=LexisChooser),

    ]
