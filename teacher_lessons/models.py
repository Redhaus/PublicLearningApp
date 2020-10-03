from django.db import models
import uuid

# Create your models here.
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel

from teacher_profile.models import TeacherProfile
from wagtail.search import index




class ClassSubject(index.Indexed, ClusterableModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    instructor = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="teacher_profile",
                                   on_delete=models.CASCADE,
                                   help_text="Select user who is the teacher connected to this profile."
                                   )

    GRADES = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    grade_level = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=GRADES,
        help_text = "Select class grade level",
    )

    class_name = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter the class title."
    )

    class_description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter the class description"
    )

    panels = [
        FieldPanel("instructor"),
        FieldPanel("class_name"),
        FieldPanel("grade_level"),
        FieldPanel("class_description"),
    ]

    def __str__(self):
        return self.class_name or ''

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"




class UserLesson(index.Indexed, ClusterableModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson_title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter the lesson title."
    )

    class_link = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Enter the lesson title."
    )



    # class_link = models.ForeignKey(ClassSubject, blank=True, null=True, related_name="class_name_lesson",
    #                                on_delete=models.SET_NULL,
    #                                help_text="Select class to this profile."
    #                                )

    lesson_description = models.TextField(
        blank=True,
        null=True,
        help_text="Enter the lesson description"
    )

    # teacher profile fields
    instructor = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="teacher_profile_lesson",
                                on_delete=models.CASCADE,
                                help_text="Select user who is the teacher who created the lesson."
                                )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    # Create Fields //////////////////
    lesson_selections = models.TextField(
        blank=True,
        null=True,
        help_text="JSON Represention of lesson selections."
    )



    panels = [

        FieldPanel("instructor"),
        FieldPanel("lesson_title"),
        FieldPanel("class_link"),
        FieldPanel("lesson_selections"),
        FieldPanel("lesson_description"),

    ]


    def __str__(self):
        return self.lesson_title or ''

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"



