from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.models import ClusterableModel

from wagtail.search import index



class CategoryEventCollection(index.Indexed, ClusterableModel):

    template = 'events/event_overview_page'


    COLLECTION_NAME = (
        ('A Survey in Western Literature I', 'A Survey in Western Literature I'),
        ('A Survey in Western Literature II', 'A Survey in Western Literature II'),
        ('A Survey in American Literature I', 'A Survey in American Literature I'),
        ('A Survey in European Literature I', 'A Survey in European Literature I'),
    )

    collection_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=COLLECTION_NAME,
        help_text = "Select which collection to this content is under ",
    )

    COLLECTION_EVENT_LIST = (
        ('ASWL1_E1', 'ASWL1_E1'),
        ('ASWL1_E2', 'ASWL1_E2'),
        ('ASWL1_E3', 'ASWL1_E3'),
        ('ASWL1_E4', 'ASWL1_E4'),
        ('ASWL1_E5', 'ASWL1_E5'),
        ('ASWL1_E6', 'ASWL1_E6'),
        ('ASWL1_E7', 'ASWL1_E7'),

        ('ASWL2_E1', 'ASWL2_E1'),
        ('ASWL2_E2', 'ASWL2_E2'),
        ('ASWL2_E3', 'ASWL2_E3'),
        ('ASWL2_E4', 'ASWL2_E4'),
        ('ASWL2_E5', 'ASWL2_E5'),
        ('ASWL2_E6', 'ASWL2_E6'),
        ('ASWL2_E7', 'ASWL2_E7'),

        ('ASAL1_E1', 'ASAL1_E1'),
        ('ASAL1_E2', 'ASAL1_E2'),
        ('ASAL1_E3', 'ASAL1_E3'),
        ('ASAL1_E4', 'ASAL1_E4'),
        ('ASAL1_E5', 'ASAL1_E5'),
        ('ASAL1_E6', 'ASAL1_E6'),
        ('ASAL1_E7', 'ASAL1_E7'),

        ('ASEL1_E1', 'ASEL1_E1'),
        ('ASEL1_E2', 'ASEL1_E2'),
        ('ASEL1_E3', 'ASEL1_E3'),
        ('ASEL1_E4', 'ASEL1_E4'),
        ('ASEL1_E5', 'ASEL1_E5'),
        ('ASEL1_E6', 'ASEL1_E6'),
        ('ASEL1_E7', 'ASEL1_E7'),
    )

    collection_event = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=COLLECTION_EVENT_LIST,
        help_text = "Select which event (e1 - e7) this content is under ",
    )


    event_title = models.CharField(max_length=120, blank=True, null=True, help_text="Enter the title of your event.")
    event_descriptor = models.TextField(blank=True, null=True, help_text="Enter a one-sentence description of the content and goal of your event.")
    quotation = models.TextField(blank=True, null=True, help_text="Enter a quotation that exemplifies this event.")
    quotation_author = models.CharField(max_length=50, blank=True, null=True, help_text="Enter the author or source of the quotation.")
    quote_source = RichTextField(features=['bold', 'italic'], blank=True, null=True, help_text="Enter the citation for the source of this quotation.")
    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Upload an image for the author of the quotation."
    )

    panels = [

        MultiFieldPanel(
            [
                FieldPanel("collection_name", classname="col6"),
                FieldPanel("collection_event", classname="col6"),
                FieldPanel("event_title", classname="col12 line"),
                FieldPanel("event_descriptor"),
            ],
            heading="Event Info",
        ),

        # group together all the panels for banner in a multi field panel
        MultiFieldPanel(
            [
                FieldPanel("quotation"),
                FieldPanel("quotation_author"),
                FieldPanel("quote_source"),
                ImageChooserPanel("author_image"),
            ],
            heading="Quote Options",
        ),
    ]

    def __str__(self):
        return self.event_title or ''

    search_fields = [
        index.SearchField('event_title', partial_match=True),
    ]

    # this is just admin naming for page Type single and plural
    class Meta:
        verbose_name = "Event Overview"
        verbose_name_plural = "Event Overviews"








