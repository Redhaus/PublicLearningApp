# Register models in django admin for bulk edits
from django.contrib import admin
from .models import PrimaryFocus, FurtherExplorations

# register in django admin
admin.site.register(PrimaryFocus)
admin.site.register(FurtherExplorations)

