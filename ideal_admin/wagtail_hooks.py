"""File: core/wagtail_hooks.py."""

from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks


# create hook for custom css for admin
@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/custom.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/custom_admin.css")
    )