from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup
)

from .models import ReadingCategory, ExtensionCommandType, ContinualGoalStandardType
from assignment_types.models import AssignmentTypes
# from events.models import CategoryEventCollection

# Register models in django admin for bulk edits
from django.contrib import admin
# from .models import Lexis

# register in django admin
admin.site.register(ReadingCategory)
admin.site.register(ExtensionCommandType)
# admin.site.register(PerformanceTypeCategory)
admin.site.register(ContinualGoalStandardType)




#
class AssignmentTypesModelAdmin(ModelAdmin):

    model = AssignmentTypes
    menu_label = "Assignment Types"
    menu_icon = "success"
    menu_order = 111
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "feat", "description")
    search_fields = ("title", "feat", "verb")
    list_filter = ("verb", "title",)



# Register your models for the admin of the shared support data
class ReadingCategoryModelAdmin(ModelAdmin):

    model = ReadingCategory
    menu_label = "Reading Category"
    menu_icon = "tag"
    menu_order = 108
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("category_name",)
    search_fields = ("category_name",)


# Register your models for the admin
class ExtensionCommandTypeModelAdmin(ModelAdmin):

    model = ExtensionCommandType
    menu_label = "Extension Command Type"
    menu_icon = "placeholder"
    menu_order = 109
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("command_name",)
    search_fields = ("command_name__",)



# Register your models for the admin
class ContinualGoalStandardTypeModelAdmin(ModelAdmin):

    model = ContinualGoalStandardType
    menu_label = "Continual Goal Standard Type"
    menu_icon = "success"
    menu_order = 111
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("standard_type",)
    search_fields = ("standard_type",)


# group all admin models
class MyModelAdminGroup(ModelAdminGroup):
    menu_label = 'Support Data'
    menu_icon = 'link' # change as required
    menu_order = 101 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ReadingCategoryModelAdmin,
             ExtensionCommandTypeModelAdmin,
             ContinualGoalStandardTypeModelAdmin,
             AssignmentTypesModelAdmin,

             )

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(MyModelAdminGroup)




