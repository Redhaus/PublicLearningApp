# Register models in django admin for bulk edits
from django.contrib import admin
from .models import CategoryEventCollection

# register in django admin
admin.site.register(CategoryEventCollection)

