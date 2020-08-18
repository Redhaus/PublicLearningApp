from wagtail.core import hooks
from .views import (EventChooserViewSet,
                    TeacherChooserViewSet,
                    ReadingChooserViewSet,
                    ExtensionChooserViewSet,
                    ContinualGoalChooserViewSet)


# class PerformanceTypeChooserViewSet(ModelChooserViewSet):
#     icon = 'tag'
#     model = PerformanceTypeCategory
#     page_title = _("Choose An Performance Type")
#     per_page = 20
#     order_by = 'performance_type'
#     # fields = ['collection_name', 'collection_event']

# Register each viewset so it can be used as a widget


# @hooks.register('register_admin_viewset')
# def register_event_chooser_viewset():
#     return PerformanceTypeChooserViewSet('performance_chooser', url_prefix='performance_chooser')
#


@hooks.register('register_admin_viewset')
def register_event_chooser_viewset():
    return EventChooserViewSet('event_chooser', url_prefix='event-chooser')


@hooks.register('register_admin_viewset')
def register_reading_chooser_viewset():
    return ReadingChooserViewSet('reading_chooser', url_prefix='reading-chooser')


@hooks.register('register_admin_viewset')
def register_extension_chooser_viewset():
    return ExtensionChooserViewSet('extension_chooser', url_prefix='extension-chooser')


@hooks.register('register_admin_viewset')
def register_goal_chooser_viewset():
    return ContinualGoalChooserViewSet('continualgoal_chooser', url_prefix='continualgoal-chooser')


@hooks.register('register_admin_viewset')
def register_teacher_chooser_viewset():
    return TeacherChooserViewSet('teacher_chooser', url_prefix='teacher-chooser')


# @hooks.register('register_admin_viewset')
# def register_lexis_chooser_viewset():
#     return SchoolChooserViewSet('school_chooser', url_prefix='school-chooser')
