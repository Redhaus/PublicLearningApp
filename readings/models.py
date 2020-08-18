from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel, \
    InlinePanel
from wagtail.core.fields import RichTextField, StreamField
# from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.models import Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.images.edit_handlers import ImageChooserPanel

# model.admin
from modelcluster.models import ClusterableModel
from chooser_panels.widgets import EventChooser, ReadingChooser

from wagtail.search import index

# for tags imports
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager




# Primary Readings ////////////////////////////////////////////


# M2M




# class Keywords(blocks.TextBlock):
#     class Meta:
#
#         icon = "edit"
#         label = "Keywords"

# Tags are many to many tables like observables
# class PrimaryFocusTag(TaggedItemBase):
#
#     content_object = ParentalKey(
#         'PrimaryFocus',
#         related_name='primary_tags',
#         on_delete=models.CASCADE,
#
#     )


# #
# # # make this a category
# class KeyTag(Orderable):
#     page = ParentalKey(
#         "PrimaryFocus",
#         related_name="key_tags",
#         on_delete=models.CASCADE,
#     )
#
#     tag = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True,
#     )
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("tag"),
#     ]



class Keywords(blocks.TextBlock):
    class Meta:

        icon = "edit"
        label = "Keywords"



class PrimaryFocus(index.Indexed, ClusterableModel):
    template = "readings/primary_focus_page.html"

    # Create StreamFields //////////////////
    keywords = StreamField(
        [("Keywords", Keywords()), ],
        null=True,
        blank=True,
        help_text="Enter key terms and concepts related to this Primary Reading"

    )


    # Create Fields //////////////////
    event_collection = models.ForeignKey(
        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text = "Enter even collection this to which this reading belongs."

    )

    author_dob = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter the author’s date of birth and date of death."

    )

    translator_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Enter the full name of the translator."

    )

    author_first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text = "Enter the author’s first name."
    )

    author_last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Enter the author’s last name."
    )

    title_major = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter the full title of the major work."
    )

    synopsis = RichTextField(features=['bold', 'italic', 'link'], blank=True, null=True, help_text = "Enter a synopsis for the major work with at least one secondary source reference.")

    purchase_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter a link to where the work can be ordered."

    )


    LEVEL = (('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced'), )

    level_ability = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=LEVEL,
        help_text="Select the reading level of the major work."
    )

    # Create dropdown options
    page_count = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the number of pages in the major work."
    )

    # needs page chooser
    reading_category = models.ForeignKey(
        "categories.ReadingCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Select or create a reading category."
    )

    source = RichTextField(features=['bold', 'italic', 'link'], blank=True, null=True,  help_text="Enter, MLA source of the work")

    book_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Upload an image for the book cover."
    )

    # Search Fields
    # search_fields = Page.search_fields + [
    #     index.SearchField('keywords'),
    #     # index.FilterField('date'),
    # ]


    panels = [

        FieldPanel("event_collection", widget=EventChooser),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("title_major", classname='col12 line'),
                FieldPanel("synopsis", classname='col12 line'),
                FieldPanel("translator_name", classname='col12 line'),

                FieldPanel("level_ability", classname='col6 line'),
                FieldPanel("page_count", classname='col6 line'),
                FieldPanel("reading_category", widget=ReadingChooser, classname='col6'),
                ImageChooserPanel("book_image", classname='col6'),

            ]),

        ], heading='Book Info'),


        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("author_first_name", classname="col6 line"),
                FieldPanel("author_last_name", classname='col6 line'),
                FieldPanel("author_dob", classname='col12'),
            ]),

        ], heading='Author Info'),

        # FieldPanel("tags"),

        StreamFieldPanel("keywords"),
        FieldPanel("purchase_link"),
        FieldPanel("source"),

        # FieldPanel("title_major"),
        # FieldPanel("author_first_name"),
        # FieldPanel("author_last_name"),
        # FieldPanel("author_dob"),
        # FieldPanel("synopsis"),
        # FieldPanel("level_ability"),
        # FieldPanel("page_count"),
        # FieldPanel("reading_category", widget=ReadingChooser),
        # ImageChooserPanel("book_image"),

    ]

    def __str__(self):
        return self.title_major or ''

    search_fields = [
        index.SearchField('title_major', partial_match=True),
    ]



    class Meta:
        verbose_name = "Primary Focus"
        verbose_name_plural = "Primary Focuses"

# Further Exploration ////////////////////////////////////////////











# class FurtherExplorationTag(TaggedItemBase):
#
#     content_object = ParentalKey(
#         'FurtherExplorations',
#         related_name='further_exploration_tags',
#         on_delete=models.CASCADE,
#
#     )



# MINOR READINGS
class FurtherExplorations(index.Indexed, ClusterableModel):
    template = "readings/further_explorations_page.html"



    # tags = ClusterTaggableManager(through=FurtherExplorationTag, blank=True)
    # Create StreamFields //////////////////
    keywords = StreamField(
        [("Keywords", Keywords()), ], null=True, blank=True,
        help_text="Enter key terms and concepts related to this resource."

    )


    # Create Fields //////////////////
    event_collection = models.ForeignKey(
        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Select event to which this resource belongs."
    )

    author_dob = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter resource author's date of birth."

    )

    author_first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Enter resource author's first name."

    )

    author_last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Enter resource author's last name."

    )

    title_minor = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter the full title of the minor work."
    )


    translator_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Enter the full name of the translator."
    )

    excerpt = RichTextField(features=['bold', 'italic'], blank=True, null=True,
                            help_text="Enter an excerpt from the beginning of the minor work."
                            )

    resource_link = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Enter resource's link."

    )

    source = RichTextField(features=['bold', 'italic', 'link'], blank=True, null=True,
                           help_text="Enter, MLA source of the work")

    # needs page chooser
    reading_category = models.ForeignKey(
        "categories.ReadingCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Enter the category of this resource."

    )


    # Search Fields
    # search_fields = Page.search_fields + [
    #     index.SearchField('keywords'),
    #     # index.FilterField('date'),
    # ]


    panels = [

        FieldPanel("event_collection", widget=EventChooser),
        # FieldPanel("title_minor"),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("title_minor", classname="col12 line"),
                FieldPanel("translator_name", classname='col12 line'),

                FieldPanel("excerpt", classname='col12 line'),
                FieldPanel("reading_category", widget=ReadingChooser, classname='col12'),

                # FieldPanel("author_dob", classname='col12'),
            ]),
        ], heading='Resource Info'),


        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("author_first_name", classname="col6 line"),
                FieldPanel("author_last_name", classname='col6 line'),
                FieldPanel("author_dob", classname='col12'),
            ]),

        ], heading='Author Info'),

        DocumentChooserPanel('resource_link'),
        # FieldPanel("tags"),
        FieldPanel("source"),
        StreamFieldPanel("keywords"),
        # FieldPanel("reading_category", widget=ReadingChooser),
        # FieldPanel("excerpt"),

    ]

    def __str__(self):
        return self.title_minor or ''

    search_fields = [
        index.SearchField('title_minor', partial_match=True),
    ]

    class Meta:
        verbose_name = "Further Exploration"
        verbose_name_plural = "Further Explorations"
