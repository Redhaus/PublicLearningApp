
from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index




# reading category model
class ReadingCategory(index.Indexed, models.Model):
    category_name = models.CharField(
        max_length=50,
        null=True,
        blank=False,
        help_text="Enter Category name such as poetry, novel, short stories, etc.",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("category_name"),
        ], heading="Readings category")

    ]

    search_fields = [
        index.SearchField('category_name', partial_match=True),
    ]

    def __str__(self):
        # string repr of this class
        return self.category_name

    class Meta:
        verbose_name = "Reading Category"
        verbose_name_plural = "Reading Categories"


# Extension Command Model
class ExtensionCommandType(index.Indexed, models.Model):
    command_name = models.CharField(
        max_length=50,
        null=True,
        blank=False,
        help_text="Enter the Extension command name such as define, read, identify, etc",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("command_name"),
        ], heading="Extension command")

    ]

    search_fields = [
        index.SearchField('command_name', partial_match=True),
    ]

    def __str__(self):
        # string repr of this class
        return self.command_name

    class Meta:
        verbose_name = "Extension Command"
        verbose_name_plural = "Extension Commands"



# Continual Goal Standards Model
class ContinualGoalStandardType(index.Indexed, models.Model):
    standard_type = models.CharField(
        max_length=50,
        null=True,
        blank=False,
        help_text="Enter standard type for Continual Goal",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("standard_type"),
        ], heading="Standard Type")
    ]

    search_fields = [
        index.SearchField('standard_type', partial_match=True),
    ]

    def __str__(self):
        # string repr of this class
        return self.standard_type

    class Meta:
        verbose_name = "Goal Standard Type"
        verbose_name_plural = "Goal Standard Types"




#
# # make this a category
# class IconCategory(index.Indexed, models.Model):
#     # page = ParentalKey("lexis.Lexis", related_name="icon_list")
#
#     # ICON_LIST = (
#     #     ('device', 'device'),
#     #     ('essential', 'essential'),
#     #     ('common', 'common'),
#     #     ('concept', 'concept'),
#     #     ('person', 'person'),
#     # )
#
#     icon_category = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="Icon category"
#     )
#
#     icon_description = models.TextField(
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="Description of category"
#     )
#
#     icon_slug = models.SlugField(
#         unique=True,
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="slug of category"
#     )
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("icon_category"),
#         FieldPanel("icon_description"),
#         FieldPanel("icon_slug"),
#     ]
#
#     def __str__(self):
#         return self.icon_category or ''
#
#     class Meta:
#         verbose_name = "Icon Category"
#         verbose_name_plural = "Icon Categories"
#




#
# # make this a category
# class PerformanceTypeCategory(index.Indexed, models.Model):
#
#
#     performance_type = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text="Enter name of the performance type."
#     )
#
#
#     performance_descriptor = models.TextField(
#         blank=True,
#         null=True,
#         help_text="Enter the description of the performance type."
#     )
#
#
#
#     # add image carousel to panels
#     panels = [
#         FieldPanel("performance_type"),
#         FieldPanel("performance_descriptor"),
#     ]
#
#     def __str__(self):
#         return self.performance_type or ''
#
#     class Meta:
#         verbose_name = "Performance Type"
#         verbose_name_plural = "Performance Types"
#







#
# class CategoryEventCollection(index.Indexed, models.Model):
#
#     COLLECTION_NAME = (
#         ('A Survey in Western Literature I', 'A Survey in Western Literature I'),
#         ('A Survey in Western Literature II', 'A Survey in Western Literature II'),
#         ('A Survey in American Literature I', 'A Survey in American Literature I'),
#         ('A Survey in European Literature I', 'A Survey in European Literature I'),
#     )
#
#     collection_name = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True,
#         choices=COLLECTION_NAME,
#         help_text = "Select which collection to this content is under ",
#     )
#
#     COLLECTION_EVENT_LIST = (
#         ('ASWL1_E1', 'ASWL1_E1'),
#         ('ASWL1_E2', 'ASWL1_E2'),
#         ('ASWL1_E3', 'ASWL1_E3'),
#         ('ASWL1_E4', 'ASWL1_E4'),
#         ('ASWL1_E5', 'ASWL1_E5'),
#         ('ASWL1_E6', 'ASWL1_E6'),
#         ('ASWL1_E7', 'ASWL1_E7'),
#
#
#         ('ASWL2_E1', 'ASWL2_E1'),
#         ('ASWL2_E2', 'ASWL2_E2'),
#         ('ASWL2_E3', 'ASWL2_E3'),
#         ('ASWL2_E4', 'ASWL2_E4'),
#         ('ASWL2_E5', 'ASWL2_E5'),
#         ('ASWL2_E6', 'ASWL2_E6'),
#         ('ASWL2_E7', 'ASWL2_E7'),
#
#
#         ('ASAL1_E1', 'ASAL1_E1'),
#         ('ASAL1_E2', 'ASAL1_E2'),
#         ('ASAL1_E3', 'ASAL1_E3'),
#         ('ASAL1_E4', 'ASAL1_E4'),
#         ('ASAL1_E5', 'ASAL1_E5'),
#         ('ASAL1_E6', 'ASAL1_E6'),
#         ('ASAL1_E7', 'ASAL1_E7'),
#
#         ('ASEL1_E1', 'ASEL1_E1'),
#         ('ASEL1_E2', 'ASEL1_E2'),
#         ('ASEL1_E3', 'ASEL1_E3'),
#         ('ASEL1_E4', 'ASEL1_E4'),
#         ('ASEL1_E5', 'ASEL1_E5'),
#         ('ASEL1_E6', 'ASEL1_E6'),
#         ('ASEL1_E7', 'ASEL1_E7'),
#     )
#
#     collection_event = models.CharField(
#         max_length=10,
#         blank=True,
#         null=True,
#         choices=COLLECTION_EVENT_LIST,
#         help_text = "Select which event (e1 - e7) this content is under ",
#
#     )
#
#     panels = [
#         MultiFieldPanel([
#             FieldPanel("collection_name"),
#             FieldPanel("collection_event"),
#         ], heading="Standard Type")
#     ]
#
#     search_fields = [
#         index.SearchField('collection_event', partial_match=True),
#     ]
#
#
#     def __str__(self):
#         # string repr of this class
#         return self.collection_event
#
#     # this is just admin naming for page Type single and plural
#     class Meta:
#         verbose_name = "Event Collection Category"
#         verbose_name_plural = "Event Collection Categories"
#







