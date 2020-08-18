
# Creating a chooser widget view for each category modelAdmin
from django.utils.translation import ugettext_lazy as _
from generic_chooser.views import ModelChooserViewSet

# import models
# from categories.models import PerformanceTypeCategory, ReadingCategory, ExtensionCommandType, ContinualGoalStandardType
from categories.models import ReadingCategory, ExtensionCommandType, ContinualGoalStandardType

from events.models import CategoryEventCollection
# from school_profile.models import SchoolProfile
# from continual_goals.models import ContinualGoals

from django.contrib.auth.models import User

# from performances.models import PerformanceTypeLink



# class PerformanceTypeChooserViewSet(ModelChooserViewSet):
#     icon = 'tag'
#     model = PerformanceTypeLink
#     page_title = _("Choose An Performance Type")
#     per_page = 20
#     # order_by = 'performance_type'
#     # fields = ['collection_name', 'collection_event']


class EventChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = CategoryEventCollection
    page_title = _("Choose An Event Category")
    per_page = 20
    order_by = 'collection_name'
    # fields = ['collection_name', 'collection_event']


class ReadingChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = ReadingCategory
    page_title = _("Choose A Reading Category")
    per_page = 20
    order_by = 'category_name'
    # fields = ['category_name']


class ExtensionChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = ExtensionCommandType
    page_title = _("Choose A Command Type")
    per_page = 20
    order_by = 'command_name'
    # fields = ['command_name']


class ContinualGoalChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = ContinualGoalStandardType
    page_title = _("Choose A Standard Type")
    per_page = 20
    order_by = 'standard_type'
    # fields = ['standard_type']


class TeacherChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = User
    page_title = _("Choose A Teacher")
    per_page = 20
    order_by = 'first_name'
    # fields = ['first_name', 'last_name', 'username']


#
#
# class SchoolChooserViewSet(ModelChooserViewSet):
#     icon = 'user'
#     model = SchoolProfile
#     page_title = _("Choose A School")
#     per_page = 20
#     order_by = 'school_name'
#     fields = ['school_name', 'primary_contact']
#
