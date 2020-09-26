from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from lexis.models import Lexis, IconList, LexisEventCollection, LexisLink
from events.models import CategoryEventCollection
from teacher_lessons.models import ClassSubject, UserLesson
from teacher_profile.models import TeacherProfile
# from readings.FurtherExplorations import FurtherExplorations
import json



# observables
# Custom serializer to add custom display fields

# class EventCollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryEventCollection
#         fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSubject
        fields = '__all__'


# class ExplorationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonExplorations
#         # fields = ['id', 'term']
#         fields = '__all__'

# class LexisSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonLexis
#         fields = '__all__'
#
# class QuestionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonQuestions
#         fields = '__all__'
#
# class PerformancesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonPerformances
#         fields = '__all__'
#
# class ExtensionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonExtensions
#         fields = '__all__'
#
# class GoalsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonGoals
#         fields = '__all__'


#
# class LexisLinkSerializer(serializers.ModelSerializer):
#
#     # this is the field that is the foreign key
#     term_link = LexisSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = LexisLink
#         fields = ['id', 'term_link']


#
# class EventLinkSerializer(serializers.ModelSerializer):
#
#     # this is the field that is the foreign key
#     event_link = EventCollectionSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = LexisEventCollection
#         fields = ['id', 'event_link']




# custom field that looks up related field
# external lookup field
# class RelatedEventField(serializers.RelatedField):
#
#     # uses existing data to refetch data needed
#     def to_representation(self, value):
#         event = CategoryEventCollection.objects.get(id=value.event_link_id)
#
#         # returns new model data in format you want
#         return {
#             "id": event.id,
#             "event": event.collection_event,
#             "part_of_speech": event.collection_name
#         }



# Struct Blocks
# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class ExplorationField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class ApplicationField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class HighlightField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class DerivationField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class LexisRootField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }


# ////////////////////////////////////


# MAIN SERIALIZER
class UserLessonSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # event_collection = serializers.StringRelatedField(many=False)
    # event_collection = EventCollectionSerializer(many=False)
    instructor = InstructorSerializer(many=False)

    print('LESSONO SERIALIER CALLED')

    def create(self, validated_data):

        print('VALIDATED DATA', validated_data)

        # get the user object of the teacher logged in creating the lesson
        user = self.context['request'].user
        teacher = TeacherProfile.objects.get(user_id=user.id)

        # get diction data["field_title"]
        # instance = Equipment.objects.create(**validated_data)

        print('VALIDATED DATA', validated_data)
        # lesson = json.dumps(validated_data["lesson_selections"])
        lesson = validated_data["lesson_selections"]
        title = validated_data["lesson_title"]


        print('LESSON', lesson)

        instance = UserLesson.objects.create(

            instructor=teacher,
            lesson_title=title,
            lesson_selections=lesson
        )

        return instance


    # class_name = ClassNameSerializer(many=False)
    # explorations = ExplorationsSerializer(many=True, read_only=True)
    # lexis = LexisSerializer(many=True)
    # questions = QuestionsSerializer(many=True)
    # performances = PerformancesSerializer(many=True)
    # extensions = ExtensionsSerializer(many=True)
    # goals = GoalsSerializer(many=True)

    # orderables
    # assign field custom serializer
    # icon_list = IconSerializer(many=True)


    # assign field custom serializer field
    # related_events = RelatedEventField(many=True, read_only=True)
    # related_events = EventLinkSerializer(many=True)

    # lexis_link = LexisLinkField(many=True, read_only=True)
    # lexis_link = LexisLinkSerializer(many=True)

    # Stream blocks
    # exploration = ExplorationField(many=True, read_only=True)
    # application = ApplicationField(many=True, read_only=True)
    # derivations = DerivationField(many=True, read_only=True)
    # lexis_root = LexisRootField(many=True, read_only=True)
    # highlight = HighlightField(many=True, read_only=True)

    # instructor = InstructorSerializer(many=False)
    # class_name = ClassNameSerializer(many=False)
    # explorations = ExplorationsSerializer(many=True)
    # lexis = LexisSerializer(many=True)
    # questions = QuestionsSerializer(many=True)
    # performances = PerformancesSerializer(many=True)
    # extensions = ExtensionsSerializer(many=True)
    # goals = GoalsSerializer(many=True)

    class Meta:
        model = UserLesson
        fields = ['id',
                  'instructor',
                  # 'class_name',
                  'lesson_title',
                  'lesson_selections',
                  # 'explorations',
                  # 'lexis',
                  # 'questions',
                  # 'performances',
                  # 'extensions',
                  # 'goals',
                  'created',
                  'updated',
                  ]

#
# {
#     "lesson_selections": {"selected_event": 1, "selected_reading": 1, "selected_related_events": [],
#                           "selected_exploration": [1, 1, 4, 4], "selected_lexis": [2, 2, 1, 1],
#                           "selected_questions": [], "selected_performances": [], "selected_extensions": [],
#                           "selected_goals": []}
#
# }
#
# {
#     "username": "redhaus",
#     "password": "REDHAUS99adm"
#
# }
#
#
# {
#     "token": "21432969f1d9b947377ffa8b5669451590b65f09",
#     "id": 1,
#     "user": "redhaus"
# }