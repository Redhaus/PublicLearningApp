from django.db import models
from django import forms
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel,  MultiFieldPanel
from wagtail.core.fields import StreamField, RichTextField

# model.admin ///////////////////////////////////
from modelcluster.models import ClusterableModel
from chooser_panels.widgets import EventChooser

from wagtail.search import index


# import streamfield blocks
from . import Derivations, LexisRoot, Highlight, Exploration, Application

# MAIN LEXIS CLASS //////////////////
class Lexis(index.Indexed, ClusterableModel):

    template = "lexis/lexis_page.html"

    # Create StreamFields //////////////////
    derivations = StreamField(
        [("Derivations", Derivations()), ],
        null=True,
        blank=True,
        help_text="Enter any alternative derivations of the term"
    )

    lexis_root = StreamField(
        [("Lexis_Root", LexisRoot()), ],
        null=True,
        blank=True,
        help_text="Enter any Latin or linguistic roots of the term"

    )

    highlight = StreamField(
        [("Highlight", Highlight()), ],
        null=True,
        blank=True,
        help_text = "Enter key points and take aways for the term"
    )

    application = StreamField(
        [("Application", Application()), ],
        null=True,
        blank=True,
        help_text="Enter core applications students should be able to perform related to the term"
    )

    exploration = StreamField(
        [("Exploration", Exploration()), ],
        null=True,
        blank=True,
        help_text="Enter ideas and concepts to explore related to the term"
    )

    # Create Fields //////////////////
    event_collection = models.ForeignKey(

        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Enter the event collection this term belongs to."
    )

    # lexis term
    term = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter the lexis term to be studied."
    )



    # Create dropdown options
    POS = (('n.', 'noun'), ('adj.', 'adjective'), ('ad.', 'adverb'), ('v', 'verb'), ('tr. v.', 'transitive verb'), ('n. pl.', 'plural noun'))
    part_of_speech = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=POS,
        help_text="Select the part of speech for the term."
    )

    # definition
    etymology = RichTextField(features=['bold', 'italic', 'link'],
                              blank=True,
                              null=True,
                              help_text="Enter the origin of the term and its historical development."
                              )

    # grouped together quote stuff
    quotation = models.TextField(blank=True, null=True, help_text="Enter a quote that utilizes the term.")
    quotation_author = models.CharField(max_length=120, blank=True, null=True, help_text="Enter the author of the quote.")
    quote_source = RichTextField(features=['bold', 'italic'], blank=True, null=True, help_text="Enter the citation for the source of this quotation.")

    # quote_source_major = models.CharField(max_length=120, blank=True, null=True, help_text="Enter the source of the quote.")
    # quote_source_minor = models.CharField(max_length=120, blank=True, null=True, help_text="Enter alternative source of the quote.")

    # icon_list = ParentalManyToManyField('categories.IconCategory', blank=False)

    # rating system
    RATING = (('gold', 'Gold Star'), ('silver', 'Silver Star'), ('red', 'Red Star'), ('blue', 'Blue Star'), ('green', 'Green Star'),)
    star_value = models.CharField(
                                  max_length=20,
                                  blank=True,
                                  null=True,
                                  choices=RATING,
                                  help_text="Enter the rating value of the term."
                                  )



    # Search Fields
    # search_fields = Page.search_fields + [
    #     index.SearchField('term'),
    #     # index.FilterField('date'),
    # ]


    # Admin Display Panels
    panels = [
        FieldPanel("event_collection", widget=EventChooser),
        # FieldPanel("term"),
        # FieldPanel("part_of_speech"),
        # FieldPanel("etymology"),

        MultiFieldPanel(
            [
                FieldPanel("term", classname="col6 line"),
                FieldPanel("part_of_speech", classname="col6 line"),
                FieldPanel("etymology", classname="col12"),

            ],
            heading="Term Info",
        ),

        MultiFieldPanel(
            [
                InlinePanel('icon_list', label="Icon List", classname="col12"),
                # FieldPanel('icon_list', widget=forms.CheckboxSelectMultiple)
            ],
            heading="Lexis Category", help_text="Select all categories that apply to the term."
        ),

        MultiFieldPanel(
            [
                # inlineLinked events attempt working
                InlinePanel('related_events',
                            label='Linked Events',
                            classname="col12 line",
                            ),
                # inlineLinked lexis links attempt working
                InlinePanel('lexis_link', label='Linked Lexis', classname="col12"),
            ],
            heading="Lexis Connections", help_text="Select all connections that apply to the term."
        ),


        # stored in separate tables
        # Many to Many Relationships for linked_evemts
        # InlinePanel('icon_list', label="Icon List"),
        # inlineLinked events attempt working
        # InlinePanel('related_events', label='Linked Events'),
        # # inlineLinked lexis links attempt working
        # InlinePanel('lexis_link', label='Linked Lexis'),


        # create streamfields for arrays stored as json




        StreamFieldPanel("derivations"),
        StreamFieldPanel("lexis_root"),
        StreamFieldPanel("highlight"),
        StreamFieldPanel("exploration"),
        StreamFieldPanel("application"),

        MultiFieldPanel(
            [
                FieldPanel("quotation"),
                FieldPanel("quotation_author"),
                FieldPanel("quote_source"),
                # FieldPanel("quote_source_minor"),
            ],
            heading="Quote Options",
        ),

        FieldPanel("star_value"),

    ]

    search_fields = [
        index.SearchField('term', partial_match=True),
    ]

    def __str__(self):
        return self.term or ''

    class Meta:
        verbose_name = "Lexis"
        verbose_name_plural = "Lexis"



