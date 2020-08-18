from django.db import models

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable

# model.admin
from modelcluster.models import ClusterableModel
from chooser_panels.widgets import EventChooser, ExtensionChooser
from lexis.models.orderables import LexisChooser

from wagtail.search import index


class ExtensionLexisLink(Orderable):

    page = ParentalKey("extensions.Extensions",
                       related_name="extension_lexis_link"
                       )
    term_link = models.ForeignKey(
        'lexis.Lexis', on_delete=models.SET_NULL, related_name='+', null=True, help_text="Enter any linked lexis terms for this extension.")

    panels = [
        # FieldPanel("term_link")
        FieldPanel("term_link", widget=LexisChooser),
    ]

    def __str__(self):
        return self.term_link.term or ''
        # return ''


class Extensions(index.Indexed, ClusterableModel):

    # Reference Template
    template = "extensions/extensions_page.html"

    # Create Fields //////////////////
    event_collection = models.ForeignKey(

        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )



    assignment_command_types = models.ForeignKey(
        "categories.ExtensionCommandType",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )


    action = RichTextField(features=['bold', 'italic'], blank=True, null=True)
    explanation = RichTextField(features=['bold', 'italic'], blank=True, null=True)


    video_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )


    # Admin Display Panels
    panels = [

        FieldPanel("event_collection", widget=EventChooser),

        MultiFieldPanel(
            [
                FieldPanel("assignment_command_types", widget=ExtensionChooser, classname="col12 line"),
                FieldPanel("action", classname="col12 line"),
                FieldPanel("explanation", classname="col12")

            ],
            heading="Extension Info",
        ),

        MultiFieldPanel(
            [
                InlinePanel('extension_lexis_link', label='Linked Lexis', classname="col12 line"),
                FieldPanel("video_link", classname="col12"),
            ],
            heading="Extension Links",
        ),

    ]

    # display name
    # return assignment_command and reference its command name property
    def __str__(self):
        return self.assignment_command_types.command_name or ''
        # return ''


    search_fields = [
        index.SearchField('action', partial_match=True),
    ]

    class Meta:
        verbose_name = "Extension"
        verbose_name_plural = "Extensions"
