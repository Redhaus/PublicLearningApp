from django.db import models
from wagtail.core import blocks
from django import forms
# Create your models here.

# make this a category
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.search import index
from wagtail.core.fields import StreamField, RichTextField

TOPIC_LIST = (
    ('device', 'device'),
    ('essential', 'essential'),
    ('common', 'common'),
    ('concept', 'concept'),
    ('person', 'person'),
    ('event', 'event'),
    ('text', 'text'),
)

CATEGORY_LIST = (

    ('essential_category', 'essential_category'),
    ('analytic_category', 'analytic_category'),
    ('journalism_category', 'journalism_category'),
    ('realworld_category', 'realworld_category'),
    ('creative_category', 'creative_category'),
    ('internet_category', 'internet_category'),
    ('visual_category', 'visual_category'),
    ('poetry_category', 'poetry_category'),
    ('business_category', 'business_category'),

)

TITLE_LIST = (

    ('Essential', 'Essential'),
    ('Analytic', 'Analytic'),
    ('Journalism', 'Journalism'),
    ('Real World', 'Real World'),
    ('Creative', 'Creative'),
    ('Internet', 'Internet'),
    ('Visual', 'Visual'),
    ('Poetry', 'Poetry'),
    ('Business and Technical', 'Business and Technical'),

)

VERB_LIST = (

    ('compose', 'compose'),
    ('create', 'create'),
    ('craft', 'craft'),

)


#
#
# class AudienceTypes(index.Indexed, models.Model):
#
#     audience = models.CharField(
#         max_length=500,
#         blank=True,
#         null=True,
#         help_text="Enter the target audience for the assignment."
#     )
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("audience"),
#
#     ]
#
#     def __str__(self):
#         return self.audience or ''
#
#     class Meta:
#         verbose_name = "Audience Type"
#         verbose_name_plural = "Audience Types"
#




class Topics(blocks.TextBlock):
    class Meta:
        icon = "edit"
        label = "Topics"








#
#
# class EssentialWriting(index.Indexed, models.Model):
#
#
#     essential_type = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="Enter name of the performance type."
#     )
#
#
#     essential_description = models.TextField(
#         blank=True,
#         null=True,
#         help_text="Enter the description of the performance type."
#     )
#
#
#     topic = models.CharField(
#         max_length=20,
#         blank=True,
#         null=True,
#         help_text="Enter the description of the performance type.",
#         choices=TOPIC_LIST
#     )
#
#
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("essential_type"),
#         FieldPanel("essential_description"),
#         FieldPanel("topic"),
#
#     ]
#
#     def __str__(self):
#         return self.essential_type or ''
#
#     class Meta:
#         verbose_name = "Essential Writing Type"
#         verbose_name_plural = "Essential Writing Types"
#




#
# class AnalyticalWriting(index.Indexed, models.Model):
#
#
#     analytical_type = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="Enter name of the performance type."
#     )
#
#
#     analytical_description = models.TextField(
#         blank=True,
#         null=True,
#         help_text="Enter the description of the performance type."
#     )
#
#
#
#     topic = models.CharField(
#         max_length=20,
#         blank=True,
#         null=True,
#         help_text="Enter the description of the performance type.",
#         choices=TOPIC_LIST
#     )
#
#
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("analytical_type"),
#         FieldPanel("analytical_description"),
#         FieldPanel("topic"),
#
#     ]
#
#     def __str__(self):
#         return self.analytical_type or ''
#
#     class Meta:
#         verbose_name = "Analytical Writing Type"
#         verbose_name_plural = "Analytical Writing Types"
#





class AssignmentTypes(index.Indexed, models.Model):


    category_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Select the category type.",
        choices=CATEGORY_LIST
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Select the type of feat.",
        choices=TITLE_LIST
    )

    verb = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Select the verb you for this feat.",
        choices=VERB_LIST
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter the description of the assignment type."
    )

    feat = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Enter the assignment feat."
    )

    topics = StreamField(
        [("Topics", Topics()), ],
        null=True,
        blank=True,
        help_text="Enter any topics to explore"
    )




    # add image carousel to panels
    panels = [

        MultiFieldPanel(
            [
                # FieldPanel("performance_type", classname="col12 line"),
                FieldPanel("category_type", classname="col6 line"),
                FieldPanel("title", classname="col6 line"),
                FieldPanel("feat", classname="col6 line"),
                FieldPanel("verb", classname="col6 line"),
                FieldPanel("description", classname="col12 line"),

                StreamFieldPanel("topics", classname="col12 line"),

                # DocumentChooserPanel("resource_link", classname="col6"),
                # DocumentChooserPanel("student_sample", classname="col6"),
                # FieldPanel("video_link", classname="col12 line-top"),
            ],
            heading="Assignment Info",
        ),


        # FieldPanel("category_type"),
        # FieldPanel("title"),
        # FieldPanel("verb"),
        # FieldPanel("description"),
        # FieldPanel("feat"),
        #
        # StreamFieldPanel("topics"),

    ]

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = "Assignment Type"
        verbose_name_plural = "Assignment Types"

#
# widgets
# __all__ = (
#     'Media', 'MediaDefiningClass', 'Widget', 'TextInput', 'NumberInput',
#     'EmailInput', 'URLInput', 'PasswordInput', 'HiddenInput',
#     'MultipleHiddenInput', 'FileInput', 'ClearableFileInput', 'Textarea',
#     'DateInput', 'DateTimeInput', 'TimeInput', 'CheckboxInput', 'Select',
#     'NullBooleanSelect', 'SelectMultiple', 'RadioSelect',
#     'CheckboxSelectMultiple', 'MultiWidget', 'SplitDateTimeWidget',
#     'SplitHiddenDateTimeWidget', 'SelectDateWidget',
# )