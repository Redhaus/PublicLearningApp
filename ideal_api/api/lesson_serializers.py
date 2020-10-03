from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from lexis.models import Lexis, IconList, LexisEventCollection, LexisLink
# from events.models import CategoryEventCollection
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

    # instructor = InstructorSerializer(many=False)



    def create(self, validated_data):

        print('VALIDATED DATA', validated_data)

        # get the user object of the teacher logged in creating the lesson

        # for api
        user = self.context['request'].user
        teacher = TeacherProfile.objects.get(user_id=user.id)

        # for browesr
        # teacher = TeacherProfile.objects.get(id=validated_data['instructor'])


        # instructor = teacher
        grade_level = validated_data["grade_level"]
        class_name = validated_data["class_name"]
        class_description = validated_data["class_description"]


        # print('LESSON', lesson)
        instance = ClassSubject.objects.create(

            instructor=teacher,
            grade_level=grade_level,
            class_name=class_name,
            class_description=class_description
        )

        return instance



    class Meta:
        model = ClassSubject
        fields = ['id',
                  'instructor',
                  'class_name',
                  'grade_level',
                  'class_description',
                  ]
        lookup_field = 'id'

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


# class ClassLinkField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "class_link": value.id,
#         }


# class ClassLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassSubject
#         fields = '__all__'


# MAIN SERIALIZER
class UserLessonSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # event_collection = serializers.StringRelatedField(many=False)
    # event_collection = EventCollectionSerializer(many=False)

    print('LESSONO SERIALIER CALLED')

    instructor = InstructorSerializer(many=False)
    # class_link = ClassLinkSerializer(many=False)

    # class_link = ClassLinkField(many=False, read_only=True)

    def create(self, validated_data):

        print('VALIDATED DATA', validated_data)

        # get the user object of the teacher logged in creating the lesson
        user = self.context['request'].user
        teacher = TeacherProfile.objects.get(user_id=user.id)
        class_id = validated_data["class_link"]
        #
        # tuple_list = list(class_id.items())
        #
        # print('LIST', tuple_list)
        # key_value = tuple_list[0]
        #
        # # print(key_value)
        #
        print('CLASSID', class_id)




        # class_subject = ClassSubject.objects.get(id=class_id)

        # get diction data["field_title"]
        # instance = Equipment.objects.create(**validated_data)

        print('VALIDATED DATA', validated_data)
        # lesson = json.dumps(validated_data["lesson_selections"])
        lesson = validated_data["lesson_selections"]
        title = validated_data["lesson_title"]
        description = validated_data["lesson_description"]
        class_link = validated_data["class_link"]



        print('LESSON', lesson)

        instance = UserLesson.objects.create(

            instructor=teacher,
            lesson_title=title,
            lesson_selections=lesson,
            class_link=class_link,
            lesson_description=description
        )

        return instance




    class Meta:
        model = UserLesson
        fields = ['id',
                  'instructor',
                  'class_link',
                  'lesson_title',
                  'lesson_selections',
                  'lesson_description',
                  'created',
                  'updated',
                  ]




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