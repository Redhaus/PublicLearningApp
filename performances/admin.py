# Register models in django admin for bulk edits
from django.contrib import admin
from .models import Performances, PerformanceLexisLink

# register in django admin
admin.site.register(Performances)
admin.site.register(PerformanceLexisLink)

