
# ///////new/////
#
from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel

# model.admin
from modelcluster.models import ClusterableModel
from chooser_panels.widgets import EventChooser
from wagtail.core.fields import RichTextField

from wagtail.search import index


class KeyQuestions(index.Indexed, ClusterableModel):
    template = "key_questions/key_questions_page.html"

    # parent_page_types = ['key_questions.KeyQuestionsList']
    # subpage_types = []

    # Create Fields //////////////////
    event_collection = models.ForeignKey(
        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Enter collection to which this question belongs."
    )

    question = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter the key question students should be able to answer by the end of the event."
    )

    explanation = RichTextField(
        features=['bold', 'italic'],
        blank=True,
        null=True,
        help_text="Enter explanation on how to teach the question."

    )

    video_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter video link on how to teach the question."
    )


    # Admin Display Panels
    panels = [
        FieldPanel("event_collection", widget=EventChooser),
        FieldPanel("question"),
        FieldPanel("explanation"),
        FieldPanel("video_link"),

    ]

    def __str__(self):
        return self.question or ''

    search_fields = [
        index.SearchField('question', partial_match=True),
    ]

    class Meta:
        verbose_name = "Key Question"
        verbose_name_plural = "Key Questions"
