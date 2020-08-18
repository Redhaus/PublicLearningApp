from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

# model.admin
from modelcluster.models import ClusterableModel
from chooser_panels.widgets import ContinualGoalChooser
from wagtail.core.fields import RichTextField

from wagtail.search import index






class ContinualGoals(index.Indexed, ClusterableModel):
    # Reference Template
    template = "continual_goals/continual_goals_page.html"


    standard_type = models.ForeignKey(
        "categories.ContinualGoalStandardType",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text = "Select the standard this goal meets."
    )

    goal = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Establish the goal that the students will be able to meet"
    )

    explanation = RichTextField(
        features=['bold', 'italic'],
        blank=True,
        null=True,
        help_text="Enter explanation on how to teach the goal."

    )

    video_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter video link on how to teach the goal."
    )

    # Admin Display Panels
    panels = [
        FieldPanel("standard_type", widget=ContinualGoalChooser),
        FieldPanel("goal"),
        FieldPanel("explanation"),
        FieldPanel("video_link"),
    ]

    def __str__(self):
        return self.goal or ''

    search_fields = [
        index.SearchField('goal', partial_match=True),
    ]

    class Meta:
        verbose_name = "Continual Goal"
        verbose_name_plural = "Continual Goals"


