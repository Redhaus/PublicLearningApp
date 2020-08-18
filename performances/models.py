from django.db import models

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks

from wagtail.core.models import Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel

# model.admin
from modelcluster.models import ClusterableModel
from lexis.models.orderables import LexisChooser
from chooser_panels.widgets import EventChooser
# from chooser_panels.widgets import EventChooser


from wagtail.search import index

from continual_goals.models import ContinualGoals
from generic_chooser.views import ModelChooserViewSet
from wagtail.core import hooks
from generic_chooser.widgets import AdminChooser



#
#
# class PerformanceTypeLink(models.Model):
#     # page = ParentalKey("performances.PerformanceFeatsLink",
#     #                    related_name="performance_type_link"
#     #                    )
#
#
#     # test_field = models.CharField(
#     #     max_length=100,
#     #     blank=True,
#     #     null=True,
#     #     help_text="Enter performance category type for this item."
#     # )
#
#
#     essential_writing = models.ForeignKey(
#         'assignments_types.EssentialWriting',
#         on_delete=models.SET_NULL,
#         related_name='+',
#         null=True,
#         help_text="Enter any lexis terms connected to this performance."
#     )
#
#     analytical_writing = models.ForeignKey(
#         'assignments_types.AnalyticalWriting',
#         on_delete=models.SET_NULL,
#         related_name='+',
#         null=True,
#         help_text="Enter any lexis terms connected to this performance."
#     )
#
#
#     panels = [
#        # user LexisChooser Panel
#         FieldPanel("essential_writing"),
#         FieldPanel("analytical_writing"),
#
#     ]



#
#
class GoalChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = ContinualGoals
    page_title = ("Choose A Continual Goal")
    per_page = 20
    order_by = 'goal'
    # fields = ['standard_type']



class GoalChooser(AdminChooser):
    choose_one_text = ('Choose a Continual Goal')
    choose_another_text = ('Choose another Continual Goal')
    link_to_chosen_text = ('Edit this Continual Goal')
    model = ContinualGoals
    choose_modal_url_name = 'goal_chooser:choose'


@hooks.register('register_admin_viewset')
def register_event_chooser_viewset():
    return GoalChooserViewSet('goal_chooser', url_prefix='goal_chooser')




# performance chooser
#
# class PerformanceTypeChooserViewSet(ModelChooserViewSet):
#     icon = 'tag'
#     model = PerformanceTypeLink
#     page_title = ("Choose An Performance Type")
#     per_page = 20
#     order_by="essential_writing"
#     # fields = ['essential_writing', 'analytical_writing']
#
# class PerformanceTypeChooser(AdminChooser):
#     choose_one_text = ('Choose a Performance Type')
#     choose_another_text = ('Choose another Performance Type')
#     link_to_chosen_text = ('Edit this Performance Type')
#     model = PerformanceTypeLink
#     choose_modal_url_name = 'performance_chooser:choose'
#
#
# @hooks.register('register_admin_viewset')
# def register_event_chooser_viewset():
#     return PerformanceTypeChooserViewSet('performance_chooser', url_prefix='performance_chooser')
#


# LexisLink
class PerformanceLexisLink(Orderable):
    page = ParentalKey("performances.Performances",
                       related_name="performance_lexis_link"
                       )
    term_link = models.ForeignKey(
        'lexis.Lexis',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        help_text="Enter any lexis terms connected to this performance."
    )


    panels = [
       # user LexisChooser Panel
        FieldPanel("term_link", widget=LexisChooser),
    ]






class PerformanceFeatsLink(Orderable):
    page = ParentalKey("performances.Performances",
                       related_name="performance_feat_link"
                       )
    performance_feats = models.CharField(
                                  max_length=500,
                                  blank=True,
                                  null=True,
                                  help_text="Enter the feat the student should be able to perform."
                                  )
    #
    # essential_writing = models.ForeignKey(
    #     'assignments_types.EssentialWriting',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     null=True,
    #     help_text="Enter any lexis terms connected to this performance."
    # )
    #
    # analytical_writing = models.ForeignKey(
    #     'assignments_types.AnalyticalWriting',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     null=True,
    #     help_text="Enter any lexis terms connected to this performance."
    # )



    # performance_type = models.ForeignKey(
    #     'categories.PerformanceTypeCategory',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    #     help_text="Select the performance type that matches this feat."
    # )

    # performance_type = models.ForeignKey(
    #     'performances.PerformanceTypeLink',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    #     help_text="Select the performance type that matches this feat."
    # )

    continual_goal = models.ForeignKey(
        'continual_goals.ContinualGoals',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        help_text="Select the continual goal this feat achieves."
    )


    panels = [
       # user LexisChooser Panel
        FieldPanel("performance_feats",),
        # InlinePanel('performance_type_link', label='Performance Type Link', max_num=1),
        # FieldPanel("performance_type", widget=PerformanceTypeChooser),
        FieldPanel("continual_goal", widget=GoalChooser),
        # FieldPanel("essential_writing", classname="col6 line"),
        # FieldPanel("analytical_writing", classname="col6 line"),
        # FieldPanel("performance_overview", classname="col12 line"),

    ]

    def __str__(self):
        return self.performance_feats or ''


# class PerformanceFeats(blocks.TextBlock):
#     class Meta:
#
#         icon = "edit"
#         label = "Performance Feats"


class Performances(index.Indexed, ClusterableModel):
    template = "performances/performances_page.html"

    #
    # essential_writing = models.ForeignKey(
    #     'assignments_types.EssentialWriting',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     null=True,
    #     help_text="Enter any lexis terms connected to this performance."
    # )

    # Create Fields //////////////////
    event_collection = models.ForeignKey(

        "events.CategoryEventCollection",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Enter collection to which this performance belongs."
    )

    # performance_type = models.CharField(
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     help_text="Enter performance category type for this item."
    # )

    performance_description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter performance category type for this item."
    )
    performance_title = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text="Enter performance category type for this item."
    )

    performance_overview = RichTextField(features=['bold', 'italic', 'link'],
                               blank=True,
                               null=True,
                               help_text="Enter a five-sentence overview of the performance."

                               )

    performance_assignment = models.TextField(
        blank=True,
        null=True,
        help_text="Enter a one sentence description that states how the learning outcome will be met in this performance."

    )

    # Create StreamFields //////////////////
    # performance_feats = StreamField(
    #     [("Performance_Feats", PerformanceFeats()), ],
    #     null=True,
    #     blank=True,
    #     help_text="Enter feats students should be able to perform."
    # )

    # document link//////////////////////////////
    resource_link = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Enter feats students should be able to perform."

    )

    # document link//////////////////////////////
    student_sample = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Upload samples of student work that successfully demonstrate this performance."
    )

    # rating system
    # rating system
    RATING = (('gold', 'Gold Star'), ('silver', 'Silver Star'), ('red', 'Red Star'), ('blue', 'Blue Star'), ('green', 'Green Star'),)
    star_value = models.CharField(
                                  max_length=20,
                                  blank=True,
                                  null=True,
                                  choices=RATING,
                                  help_text="Enter the rating value of the performance."
                                  )

    video_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide a link that demonstrates how to teach this performance."

    )

    # Admin Display Panels
    panels = [

        FieldPanel("event_collection", widget=EventChooser),
        # FieldPanel("essential_writing"),


        MultiFieldPanel(
            [
                # FieldPanel("performance_type", classname="col12 line"),
                FieldPanel("performance_title", classname="col12 line"),
                FieldPanel("performance_description", classname="col12 line"),
                FieldPanel("performance_assignment", classname="col12 line"),
                FieldPanel("performance_overview", classname="col12 line"),

                # DocumentChooserPanel("resource_link", classname="col6"),
                # DocumentChooserPanel("student_sample", classname="col6"),
                # FieldPanel("video_link", classname="col12 line-top"),
            ],
            heading="Performance Info",
        ),

        # inlineLinked lexis links attempt working
        InlinePanel('performance_lexis_link', label='Linked Lexis'),
        InlinePanel('performance_feat_link', label='Performance Feats'),

        # StreamFieldPanel("performance_feats"),

        MultiFieldPanel(
            [
                DocumentChooserPanel("resource_link", classname="col12 line"),
                DocumentChooserPanel("student_sample", classname="col12 line"),
                FieldPanel("video_link", classname="col12"),
            ],
            heading="Resources & Samples",
        ),

        FieldPanel("star_value"),


    ]

    def __str__(self):
        return self.performance_title or ''

    search_fields = [
        index.SearchField('performance_title', partial_match=True),
    ]

    class Meta:
        verbose_name = "Performance"
        verbose_name_plural = "Performances"
