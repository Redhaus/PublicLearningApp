# from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
# from modelcluster.fields import ParentalKey
# from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
# from wagtail.core.models import Orderable
#
# # from IdealEducationVue.chooser_panels.widgets import EventChooser
#
# # MAIN LEXIS CLASS //////////////////
# from modelcluster.models import ClusterableModel
# from wagtail.search import index
# from teacher_profile.models import TeacherProfile
#
#
# # # FURTHER EXPLORATION
# class LessonExplorations(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_explorations"
#                        )
#
#     exploration_links = models.ForeignKey(
#         "readings.FurtherExplorations",
#         on_delete=models.SET_NULL,
#         related_name='exploration_linked',
#         null=True,
#         help_text="Select all explorations for this lesson."
#     )
#
#     # custom chooser panel
#     panels = [
#         FieldPanel("exploration_links"),
#     ]
#
#
#
# # # LEXIS
# class LessonLexis(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_lexis"
#                        )
#
#     lexis_links = models.ForeignKey(
#         'lexis.Lexis',
#         on_delete=models.SET_NULL,
#         related_name='lexis_linked',
#         null=True,
#         help_text="Select any related lexis terms."
#     )
#
#     panels = [
#         FieldPanel("lexis_links"),
#
#     ]
#
#
#
#
# # # KEY QUESTIONS
# class LessonQuestions(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_questions"
#                        )
#
#     question_links = models.ForeignKey(
#         "key_questions.KeyQuestions",
#         on_delete=models.SET_NULL,
#         related_name='question_linked',
#         null=True,
#         help_text="Select questions for this lesson."
#     )
#
#     # custom chooser panel
#     panels = [
#         FieldPanel("question_links"),
#     ]
#
#
#
# # # Performances
# class LessonPerformances(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_performances"
#                        )
#
#     performance_links = models.ForeignKey(
#         "performances.Performances",
#         on_delete=models.SET_NULL,
#         related_name='performance_linked',
#         null=True,
#         help_text="Select any Performances for the lesson."
#     )
#
#     # custom chooser panel
#     panels = [
#         FieldPanel("performance_links"),
#     ]
# #
# #
#
#
#
#
# class LessonExtensions(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_extensions"
#                        )
#
#     extension_links = models.ForeignKey(
#         "extensions.Extensions",
#         on_delete=models.SET_NULL,
#         related_name='extension_linked',
#         null=True,
#         help_text="Select all related events."
#     )
#
#     # custom chooser panel
#     panels = [
#         FieldPanel("extension_links"),
#     ]
#
#
#
#
# # Goals
# class LessonGoals(Orderable):
#     page = ParentalKey("user_lessons.UserLesson",
#                        related_name="lesson_goals"
#                        )
#
#     goal_links = models.ForeignKey(
#         "continual_goals.ContinualGoals",
#         on_delete=models.SET_NULL,
#         related_name='goal_linked',
#         null=True,
#         help_text="Select goals related to the lesson."
#     )
#
#     # custom chooser panel
#     panels = [
#         FieldPanel("goal_links"),
#     ]
#
#
#
# class ClassSubject(index.Indexed, ClusterableModel):
#
#     instructor = models.ForeignKey(TeacherProfile, blank=False, null=True, related_name="teacher_profile",
#                                    on_delete=models.CASCADE,
#                                    help_text="Select user who is the teacher connected to this profile."
#                                    )
#
#     class_name = models.CharField(
#         max_length=500,
#         blank=False,
#         null=False,
#         help_text="Enter the class title."
#     )
#
#     class_description = models.TextField(
#         blank=True,
#         null=True,
#         help_text="Enter the class description"
#     )
#
#     panels = [
#         FieldPanel("instructor"),
#         FieldPanel("class_name"),
#         FieldPanel("class_description"),
#     ]
#
#     def __str__(self):
#         return self.class_name or ''
#
#     class Meta:
#         verbose_name = "Class"
#         verbose_name_plural = "Classes"
#
#
#
#
#
#
# class UserLesson(index.Indexed, ClusterableModel):
#     lesson_title = models.CharField(
#         max_length=500,
#         blank=False,
#         null=False,
#         help_text="Enter the lesson title."
#     )
#
#     # class_name = models.CharField(
#     #     max_length=200,
#     #     blank=True,
#     #     null=True,
#     #     help_text="Enter the class this lesson is for"
#     # )
#
#     class_name = models.ForeignKey(ClassSubject, blank=False, null=True, related_name="class_name_lesson",
#                                    on_delete=models.SET_NULL,
#                                    help_text="Select class to this profile."
#                                    )
#
#     # teacher profile fields
#     instructor = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="teacher_profile_lesson",
#                                 on_delete=models.CASCADE,
#                                 help_text="Select user who is the teacher who created the lesson."
#                                 )
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#
#     # Create Fields //////////////////
#     event_collection = models.ForeignKey(
#
#         "events.CategoryEventCollection",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="+",
#         help_text="Enter the event for this lesson."
#     )
#
#
#     primary_reading = models.ForeignKey(
#         "readings.PrimaryFocus",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="+",
#         help_text="Enter the primary reading for this lesson."
#     )
#
#
#     panels = [
#
#         FieldPanel("instructor"),
#         FieldPanel("lesson_title"),
#         FieldPanel("class_name"),
#         FieldPanel("event_collection"),
#         FieldPanel("primary_reading"),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_explorations", label='Exploration Links',),
#             ],
#             heading="Exploration Selections",
#         ),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_lexis", label='Lexis Links'),
#             ],
#             heading="Lexis Selections",
#         ),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_questions", label='Question Links'),
#             ],
#             heading="Question Selections",
#         ),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_performances", label='Performance Links'),
#             ],
#             heading="Performances Selections",
#         ),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_extensions", label='Extension Links'),
#             ],
#             heading="Extensions Selections",
#         ),
#
#         MultiFieldPanel(
#             [
#                 InlinePanel("lesson_goals", label='Goals Links'),
#             ],
#             heading="Goals Selections",
#         ),
#
#
#
#
#
#
#         # FieldPanel("part_of_speech", classname="col6 line"),
#         # FieldPanel("etymology", classname="col12"),
#
#
#     ]
#
#
#     def __str__(self):
#         return self.lesson_title or ''
#
#     class Meta:
#         verbose_name = "Lesson"
#         verbose_name_plural = "Lessons"
#
#
#
#
#     # template = "lexis/lexis_page.html"
#
#
