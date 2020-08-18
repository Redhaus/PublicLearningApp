from django.db import models
from django.contrib.auth.models import User

from wagtail.search import index

# choice select vars
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from chooser_panels.widgets import TeacherChooser


# selections var
LEVEL = (
    ('K-5', 'K-5'),
    ('6-8', '6-8'),
    ('9-12', '9-12'),
    ('K-12', 'K-12'),
    ('K-8', 'K-8'),
    ('6-12', '6-12')
)

# Create school model
class SchoolProfile(index.Indexed, models.Model):

    # get school data needed from user
    school_name = models.CharField(max_length=100, blank=True, null=True,  help_text="Enter the name of the learning institution.")
    grade_level = models.CharField(max_length=40, blank=True, choices=LEVEL, help_text="Enter the grade levels of the learning institution.")

    # create FK field for user
    # possible filter one to one with this User.objects.get(id=1)
    primary_contact = models.OneToOneField(User, blank=True, null=True, related_name="admin_profile",
                                           on_delete=models.CASCADE,
                                            help_text = "Enter primary user and contact at the learning institution.")

    subjects = models.TextField(blank=True, null=True, help_text = "Enter the subjects taught at your learning institution.")

    # CONTACT
    phone_number = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter primary contact phone number at the learning institution.")
    street_address = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter address of the learning institution.")
    city = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter the city of the learning institution.")
    postcode = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter the city of the learning institution.")
    province = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter the province of the learning institution.")
    country = models.CharField(max_length=200, blank=True, null=True, help_text = "Enter the country of the learning institution.")

    panels = [
        FieldPanel('school_name'),
        FieldPanel('grade_level'),
        FieldPanel('primary_contact', widget=TeacherChooser),

        FieldPanel('subjects'),

        MultiFieldPanel(
            [
                FieldPanel('phone_number'),
                FieldPanel('street_address'),
                FieldPanel('city'),
                FieldPanel('postcode'),
                FieldPanel('province'),
                FieldPanel('country'),
            ],
            heading="Contact Information",
        ),

    ]

    # related teachers get with a function?

    # repr so it shows the school name
    def __str__(self):
        return self.school_name

    # search
    search_fields = [
        index.SearchField('school_name', partial_match=True),
    ]


    class Meta:
        verbose_name = ('School profile')
        verbose_name_plural = ('School profiles')


