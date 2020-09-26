# from django.contrib import admin
#
# from django.contrib import admin
# from django.utils.safestring import mark_safe
# from wagtail.contrib.modeladmin.options import (
#     ModelAdmin,
#     modeladmin_register,
#     ModelAdminGroup)
#
# # remove html tags from list_display items
# from django.utils.html import strip_tags
#
# # Register your models here.
# from .models import ClassSubject, UserLesson
#
# # register in django admin
# admin.site.register(ClassSubject)
# admin.site.register(UserLesson)
#
#
# # Register your models for the admin
# class UserLessonModelAdmin(ModelAdmin):
#
#     model = UserLesson
#     menu_label = "User Lesson"
#     menu_icon = "doc-full-inverse"
#     menu_order = 106
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ("lesson_title", "instructor", "class_name")
#     search_fields = ("lesson_title", "class_name")
#
#     # list_filter = ("level_ability", "reading_category", "event_collection", )
#     list_per_page = 20
# # modeladmin_register(PrimaryFocusModelAdmin)
#
#
#
#
# # Register your models for the admin
# class ClassSubjectModelAdmin(ModelAdmin):
#
#     model = ClassSubject
#     menu_label = "Class Subject"
#     menu_icon = "site"
#     menu_order = 111
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ("instructor", "class_name", "class_description")
#     search_fields = ("class_name", "class_description")
#     # list_filter = ("reading_category", "event_collection",)
#     list_per_page = 20
#
#     # display richtext without tags
#     # def reading_excerpt(self, obj):
#     #     ex = obj.excerpt
#     #     my_excerpt = strip_tags(ex)
#     #     return mark_safe(my_excerpt) or ''
#
#
# # modeladmin_register(FurtherExplorationsModelAdmin)
#
#
#
#
# class LessonAdminGroup(ModelAdminGroup):
#     menu_label = 'Lessons'
#     menu_icon = 'folder' # change as required
#     menu_order = 109 # will put in 3rd place (000 being 1st, 100 2nd)
#     items = (
#             # EventOverviewModelAdmin,
#             ClassSubjectModelAdmin,
#             UserLessonModelAdmin,
#
#
#     )
#
# # When using a ModelAdminGroup class to group several ModelAdmin classes together,
# # you only need to register the ModelAdminGroup class with Wagtail:
# modeladmin_register(LessonAdminGroup)