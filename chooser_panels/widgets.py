
from django.utils.translation import ugettext_lazy as _
from generic_chooser.widgets import AdminChooser

# import models
from categories.models import  ExtensionCommandType, ContinualGoalStandardType, ReadingCategory
from events.models import CategoryEventCollection
# from continual_goals.models import ContinualGoals
# from performances.models import PerformanceTypeLink

from django.contrib.auth.models import User





# class PerformanceTypeChooser(AdminChooser):
#     choose_one_text = _('Choose a Performance Type')
#     choose_another_text = _('Choose another Performance Type')
#     link_to_chosen_text = _('Edit this Performance Type')
#     model = PerformanceTypeLink
#     choose_modal_url_name = 'performance_chooser:choose'

class EventChooser(AdminChooser):
    choose_one_text = _('Choose a Event')
    choose_another_text = _('Choose another Event')
    link_to_chosen_text = _('Edit this Event')
    model = CategoryEventCollection
    choose_modal_url_name = 'event_chooser:choose'

class ExtensionChooser(AdminChooser):
    choose_one_text = _('Choose a Extension Command')
    choose_another_text = _('Choose another Extension Command')
    link_to_chosen_text = _('Edit this Extension Command')
    model = ExtensionCommandType
    choose_modal_url_name = 'extension_chooser:choose'

class ReadingChooser(AdminChooser):
    choose_one_text = _('Choose a Reading Category')
    choose_another_text = _('Choose another Reading Category')
    link_to_chosen_text = _('Edit this Reading Category')
    model = ReadingCategory
    choose_modal_url_name = 'reading_chooser:choose'

class ContinualGoalChooser(AdminChooser):
    choose_one_text = _('Choose a Continual Goal')
    choose_another_text = _('Choose another Continual Goal')
    link_to_chosen_text = _('Edit this Continual Goal')
    model = ContinualGoalStandardType
    choose_modal_url_name = 'continualgoal_chooser:choose'


class TeacherChooser(AdminChooser):
    choose_one_text = _('Choose a Teacher')
    choose_another_text = _('Choose another Teacher')
    link_to_chosen_text = _('Edit this Teacher')
    model = User
    choose_modal_url_name = 'teacher_chooser:choose'


    # functions to edit backlink for each model in chooser panel
    # def get_edit_item_url(self, item):
    #     return reverse('admin:edit', args=('categories', 'categoryeventcollection', quote(item.pk)))




#
#
# class SchoolChooser(AdminChooser):
#     choose_one_text = _('Choose a School')
#     choose_another_text = _('Choose another School')
#     link_to_chosen_text = _('Edit this School')
#     model = SchoolProfile
#     choose_modal_url_name = 'school_chooser:choose'



