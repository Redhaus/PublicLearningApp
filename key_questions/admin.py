# Register models in django admin for bulk edits
from django.contrib import admin
from .models import KeyQuestions

# register in django admin
admin.site.register(KeyQuestions)

