from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.contrib.auth.models import User
from school_profile.models import SchoolProfile

# from invitations.models import Invitation
# from django.contrib.auth.models import Group

from chooser_panels.widgets import TeacherChooser
from school_profile.models.school_chooser import SchoolChooser

from wagtail.search import index


LEVEL = (
    ('K-5', 'K-5'),
    ('6-8', '6-8'),
    ('9-12', '9-12'),
    ('K-12', 'K-12'),
    ('K-8', 'K-8'),
    ('6-12', '6-12')
)

# Teacher profile extension of User
class TeacherProfile(index.Indexed, models.Model):

    # teacher profile fields
    user = models.OneToOneField(User, blank=False, null=True, related_name="teacher_profile",
                                on_delete=models.CASCADE,
                                help_text="Select user who is the teacher connected to this profile."
                                )
    full_name = models.CharField(max_length=200, null=True, blank=False,
                                 help_text="Enter teacher's full name."
                                 )
    teacher_bio = models.TextField(null=True, blank=True,
                                   help_text="Enter teacher's bio."
                                   )

    subjects = models.TextField(blank=True, null=True, help_text = "Enter the subjects you teach.")


    school_name = models.ForeignKey(SchoolProfile, blank=True, null=True,
                                    on_delete=models.SET_NULL,
                                    help_text="Select the school to which the teacher is connected."
                                    )
    grade_level = models.CharField(max_length=40, blank=False, null=True, choices=LEVEL,
                                   help_text="Enter the grade level the teacher instructs."
                                   )
    profile_image = models.ForeignKey(
        # image class being referenced
        "wagtailimages.Image",
        # allows to be null in db
        null=True,
        # requires when field out in form
        blank=True,
        # on delete on image set this value to null don't cascade'
        on_delete=models.SET_NULL,
        # No special related name
        related_name="+",
        help_text="Upload profile picture."

    )

    panels = [

        FieldPanel('school_name', widget=SchoolChooser),
        FieldPanel('user', widget=TeacherChooser),

        # FieldPanel('school_name'),
        # FieldPanel('user'),

        MultiFieldPanel(
            [
                FieldPanel('full_name'),
                FieldPanel('teacher_bio'),
                FieldPanel('grade_level'),
                FieldPanel('subjects'),
                ImageChooserPanel('profile_image'),
            ],
            heading="Teacher Information",
        ),
    ]

    # lesson_plans orderable?

    def __str__(self):
        return self.full_name or ''

    search_fields = [
        index.SearchField('user', partial_match=True),
    ]

    class Meta:
        verbose_name = ('Teacher profile')
        verbose_name_plural = ('Teacher profiles')

