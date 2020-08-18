from django.contrib.auth.models import User, Group
from rest_framework import serializers
from performances.models import Performances, PerformanceFeatsLink, PerformanceLexisLink
from continual_goals.models import ContinualGoals

from categories.models import ExtensionCommandType
from lexis.models import Lexis
from events.models import CategoryEventCollection


# import for image link
from wagtail.documents.models import Document


# observables
# Custom searializer to add custom display fields
class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEventCollection
        fields = ['id', 'collection_name', 'collection_event']


# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
# class PerformanceFeaturesField(serializers.RelatedField):
#     def to_representation(self, value):
#         return {
#             "id": value.id,
#             "value": value.value,
#         }

# this is how you add an image link to api
class ResourceDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file']

# this is how you add an image link to api
class StudentSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file']



# class FeaturesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PerformanceFeatsLink
#         fields = ['id', 'performance_feats', 'continual_goal']


# This serializer fetches teh ContinualGoal for each feat
class CGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinualGoals
        fields = '__all__'



# continual goal uses the CG serializer above
class FeaturesSerializer(serializers.ModelSerializer):
    continual_goal = CGSerializer(many=False, read_only=True)

    class Meta:
        model = PerformanceFeatsLink
        fields = ['id', 'performance_feats', 'continual_goal']
        # fields = '__all__'
        # exclude = ('page', 'sort_order')

    #
    # def get_continual_goal(self, obj):
    #     qs = obj.continual_goal.all()
    #     return CGSerializer(qs, many=True, read_only=True).data


class LexisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexis
        fields = ['id', 'term']
        # fields = '__all__'


class LexisLinkSerializer(serializers.ModelSerializer):

    # this is the field that is the foreign key
    term_link = LexisSerializer(many=False, read_only=True)


    class Meta:
        model = PerformanceLexisLink
        fields = ['id', 'term_link']


#
# class LexisSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lexis
#         fields = '__all__'

# lex = Lexis.objects.prefetch_related().all()
# print('LEX: ', lex)
# lex = ContinualGoals.objects.prefetch_related().all()
# print(all_goals)
#
#
# class LexisLinkField(serializers.RelatedField):
#
#     # uses existing data to refetch data needed
#
#     def to_representation(self, value):
#         # lex = LexisSerializer(many=False, read_only=True)
#         # print('LEX: ', lex)
#
#         # term = lex.objects.fitler(id=value.term_link_id)
#         term=lex.filter(id=value.term_link_id).first()
#         # returns new model data in format you want
#
#         return {
#             "id": term.id,
#             "term": term.term,
#             "part_of_speech": term.part_of_speech
#         }


#     # WORKING
# class LexisLinkField(serializers.RelatedField):
#
#     # uses existing data to refetch data needed
#     def to_representation(self, value):
#         term = Lexis.objects.get(id=value.term_link_id)
#
#         # returns new model data in format you want
#         return {
#             "id": term.id,
#             "term": term.term,
#             "part_of_speech": term.part_of_speech
#         }

#
# all_goals = ContinualGoals.objects.prefetch_related().all()
# print(all_goals)
#
# class FeatLinkField(serializers.RelatedField):
#
#     # uses existing data to refetch data needed
#     def to_representation(self, value):
#         # term = Lexis.objects.get(id=value.term_link_id)
#
#
#
#         cg = {
#             "goal": None,
#             "id": None
#         }
#
#         if value.continual_goal_id:
#             # goals = ContinualGoals.objects.prefetch_related(id=value.continual_goal_id).first()
#             goal = all_goals.filter(id=value.continual_goal_id).first()
#
#             cg = {
#                 "goal": goal.goal,
#                 "id": goal.id
#             }
#
#
#         # returns new model data in format you want
#         return {
#             "id": value.id,
#             "performance_feats": value.performance_feats,
#             "continual_goal": cg
#         }


# MAIN SERIALIZER
class PerformancesSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    event_collection = EventCollectionSerializer(many=False)
    # performance_lexis_link = LexisLinkField(many=True, read_only=True)
    performance_lexis_link = LexisLinkSerializer(many=True)

    performance_feat_link = FeaturesSerializer(many=True)
    # performance_feat_link = FeatLinkField(many=True, read_only=True)
    resource_link = ResourceDocumentSerializer(many=False)
    student_sample = StudentSampleSerializer(many=False)


    class Meta:
        model = Performances
        fields = ['id',
                  'event_collection',
                  'performance_title',
                  'performance_description',
                  'performance_assignment',
                  'performance_overview',

                  'performance_lexis_link',
                  'performance_feat_link',

                  'resource_link',
                  'student_sample',
                  'video_link',

                  'star_value',

                  ]

