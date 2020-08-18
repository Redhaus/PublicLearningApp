from django.contrib.auth.models import User, Group
from rest_framework import serializers
from extensions.models import Extensions, ExtensionLexisLink

from categories.models import ExtensionCommandType
from events.models import CategoryEventCollection
from lexis.models import Lexis



# observables
# Custom searializer to add custom display fields
class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEventCollection
        fields = ['id', 'collection_name', 'collection_event']


# this is how you add an image link to api
class CommandTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionCommandType
        fields = ['id', 'command_name']



class LexisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexis
        fields = ['id', 'term']
        # fields = '__all__'


class LexisLinkSerializer(serializers.ModelSerializer):

    # this is the field that is the foreign key
    term_link = LexisSerializer(many=False, read_only=True)


    class Meta:
        model = ExtensionLexisLink
        fields = ['id', 'term_link']




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



# MAIN SERIALIZER EXTENSIONS
class ExtensionsSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    event_collection = EventCollectionSerializer(many=False)
    assignment_command_types = CommandTypeSerializer(many=False)
    extension_lexis_link = LexisLinkSerializer(many=True)

    # extension_lexis_link = LexisLinkField(many=True, read_only=True)

    class Meta:
        model = Extensions
        fields = ['id',
                  'event_collection',
                  'assignment_command_types',
                  'action',
                  'explanation',
                  'extension_lexis_link',
                  'video_link',

                  ]
