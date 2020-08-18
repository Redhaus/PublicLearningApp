from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup)
from .models import SchoolProfile
from teacher_profile.models import TeacherProfile


# Register models in django admin for bulk edits
from django.contrib import admin

# register in django admin
admin.site.register(TeacherProfile)
admin.site.register(SchoolProfile)

# Register your models for the admin
class TeacherAdmin(ModelAdmin):

    # reference model
    model = TeacherProfile
    # name and icon
    menu_label = "Teachers"
    menu_icon = "user"
    # position in nav
    menu_order = 290
    # settings info
    add_to_settings_menu = False
    exclude_from_explorer = False
    # fields to show and search
    list_display = ("full_name", "grade_level", "user", "school_name" )
    search_fields = ("full_name",)
    list_filter = ("school_name", )



# Register your models for the admin
class SchoolAdmin(ModelAdmin):

    model = SchoolProfile
    menu_label = "Schools"
    menu_icon = "idealhome"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("school_name", "primary_contact", "grade_level")
    search_fields = ("school_name",)
    list_filter = ("grade_level", )


class UsersAdminGroup(ModelAdminGroup):
    menu_label = 'Users'
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (TeacherAdmin,
             SchoolAdmin,
             )

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(UsersAdminGroup)