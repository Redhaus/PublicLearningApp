
from django.contrib import admin
from django.utils.safestring import mark_safe
from wagtail.contrib.modeladmin.helpers import WagtailBackendSearchHandler
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup)
from extensions.models import Extensions
from continual_goals.models import ContinualGoals
from key_questions.models import KeyQuestions
from lexis.models import Lexis
from performances.models import Performances
from readings.models import PrimaryFocus, FurtherExplorations
from events.models import CategoryEventCollection


# remove html tags from list_display items
from django.utils.html import strip_tags


# These are the model admin for all of the models

# Register your models for the admin
class CategoryEventCollectionModelAdmin(ModelAdmin):

    model = CategoryEventCollection
    menu_label = "Event Overview"
    menu_icon = "time"
    menu_order = 1
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("collection_name", "collection_event", "event_title")
    search_fields = ("collection_name", "collection_event", "event_title")
    list_filter = ("collection_name", )



# Register your models for the admin
class ContinualGoalsModelAdmin(ModelAdmin):

    model = ContinualGoals
    menu_label = "Continual Goals"
    menu_icon = "pick"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("goal", "standard_type", "goal_explanation")
    search_fields = ("goal", "standard_type__standard_type")
    list_filter = ("standard_type", )
    list_per_page = 20

    # display richtext without tags if needed for actions
    def goal_explanation(self, obj):
        ex = obj.explanation
        my_explanation = strip_tags(ex)
        return mark_safe(my_explanation) or ''








# Register your models for the admin
class ExtensionsModelAdmin(ModelAdmin):

    model = Extensions
    menu_label = "Extensions"
    menu_icon = "arrows-up-down"
    menu_order = 103
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("assignment_command_types", "action", "event_collection" )
    search_fields = ("assignment_command_types__command_name", "action")
    list_filter = ("event_collection", "assignment_command_types", )
    list_per_page = 20
# modeladmin_register(ExtensionsModelAdmin)

    # display richtext without tags if needed for actions
    # def list_etymology(self, obj):
    #     et = obj.etymology
    #     my_etymology = strip_tags(et)
    #     return mark_safe(my_etymology) or ''



# Register your models for the admin
class KeyQuestionsModelAdmin(ModelAdmin):



    model = KeyQuestions
    menu_label = "Key Questions"
    menu_icon = "help"
    menu_order = 104
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("event_collection", "question")
    search_fields = ("question", )
    list_filter = ("event_collection", )
    list_per_page = 20
#
#     def event_questions(self, obj):
#
#         # create a short array of questions
#         qList = []
#         for q in obj.questions.values_list('question', flat=True):
#             if len(qList) < 3:
#                 qList.append(q)
#
#         # display that short list of questions
#         to_return = '<ul style="margin-top: 0px">'
#         # I'm assuming that there is a name field under the event.Product model. If not change accordingly.
#         to_return += '\n'.join(
#             '<li>{}</li>'.format(q) for q in qList)
#         to_return += '\n'.join('...')
#         to_return += '</ul>'
#
#         # to_return = '<ul style="margin-top: 0px">'
#         # # I'm assuming that there is a name field under the event.Product model. If not change accordingly.
#         # to_return += '\n'.join(
#         #     '<li>{}</li>'.format(q) for q in obj.questions.values_list('question', flat=True))
#         # to_return += '</ul>'
#
#
#         # question_list = obj.questions.values_list('question', flat=True)
#         # return mark_safe(to_return) or ''
#         return mark_safe(to_return) or ''
#
#
# # modeladmin_register(KeyQuestionsModelAdmin)




# Register your models for the admin
class LexisModelAdmin(ModelAdmin):

    model = Lexis
    search_handler_class = WagtailBackendSearchHandler
    menu_label = "Lexis"
    menu_icon = "list-ul"
    menu_order = 11
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("term", "part_of_speech", "event_collection", "term_etymology")
    search_fields = ("term",)
    # filter by event_collection and collection_name field
    # filter by event_collection and collection_event field
    list_filter = ("part_of_speech", "event_collection__collection_name", "event_collection__collection_event",)
    list_per_page = 20

    # display richtext without tags
    def term_etymology(self, obj):
        et = obj.etymology
        my_etymology = strip_tags(et)
        return mark_safe(my_etymology) or ''



# modeladmin_register(LexisModelAdmin)





# Register your models for the admin
class PerformancesModelAdmin(ModelAdmin):

    model = Performances
    menu_label = "Performances"
    menu_icon = "tick"
    menu_order = 104
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("performance_title", "performance_description", "event_collection")
    search_fields = ("performance_title",)
    list_filter = ("event_collection",)
    list_per_page = 20

# modeladmin_register(PerformancesModelAdmin)




# Register your models for the admin
class PrimaryFocusModelAdmin(ModelAdmin):


    model = PrimaryFocus
    menu_label = "Primary Focus"
    menu_icon = "doc-full-inverse"
    menu_order = 106
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title_major", "event_collection", "level_ability", "reading_category", "author_first_name", "author_last_name")
    search_fields = ("title_major", "author_first_name", "author_last_name")

    list_filter = ("level_ability", "reading_category", "event_collection", )
    list_per_page = 20
# modeladmin_register(PrimaryFocusModelAdmin)




# Register your models for the admin
class FurtherExplorationsModelAdmin(ModelAdmin):

    model = FurtherExplorations
    menu_label = "Further Explorations"
    menu_icon = "site"
    menu_order = 107
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title_minor", "event_collection", "reading_excerpt", "author_last_name")
    search_fields = ("title_minor", "author_last_name")
    list_filter = ("reading_category", "event_collection",)
    list_per_page = 20

    # display richtext without tags
    def reading_excerpt(self, obj):
        ex = obj.excerpt
        my_excerpt = strip_tags(ex)
        return mark_safe(my_excerpt) or ''


# modeladmin_register(FurtherExplorationsModelAdmin)




class CurriculumAdminGroup(ModelAdminGroup):
    menu_label = 'Curriculum'
    menu_icon = 'folder' # change as required
    menu_order = 100 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
            # EventOverviewModelAdmin,
            CategoryEventCollectionModelAdmin,
            PrimaryFocusModelAdmin,
            LexisModelAdmin,
            FurtherExplorationsModelAdmin,
            KeyQuestionsModelAdmin,
            PerformancesModelAdmin,
            ExtensionsModelAdmin,
            ContinualGoalsModelAdmin,

    )

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(CurriculumAdminGroup)