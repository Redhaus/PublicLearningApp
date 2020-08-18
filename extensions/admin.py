# Register models in django admin for bulk edits
from django.contrib import admin
from .models import Extensions, ExtensionLexisLink

# register in django admin
admin.site.register(Extensions)
admin.site.register(ExtensionLexisLink)

