from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from lexis.models import Lexis, IconList, LexisEventCollection, LexisLink
from events.models import CategoryEventCollection
from lexis.models import Lexis, LexisEventCollection, LexisLink, IconList



# observables
# Custom serializer to add custom display fields
class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconList
        fields = ['icons', 'id']

class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEventCollection
        fields = ['id', 'collection_name', 'collection_event']


# Observables
# READ ONLY to Display custom format data
# custom field that looks up related field
# external model lookup
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


class LexisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexis
        fields = ['id', 'term']
        # fields = '__all__'


class LexisLinkSerializer(serializers.ModelSerializer):

    # this is the field that is the foreign key
    term_link = LexisSerializer(many=False, read_only=True)

    class Meta:
        model = LexisLink
        fields = ['id', 'term_link']



class EventLinkSerializer(serializers.ModelSerializer):

    # this is the field that is the foreign key
    event_link = EventCollectionSerializer(many=False, read_only=True)

    class Meta:
        model = LexisEventCollection
        fields = ['id', 'event_link']




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
class ExplorationField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class ApplicationField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class HighlightField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class DerivationField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }

# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class LexisRootField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }


# ////////////////////////////////////


# MAIN SERIALIZER
class LexisSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # event_collection = serializers.StringRelatedField(many=False)
    event_collection = EventCollectionSerializer(many=False)
    icon_list = IconSerializer(many=True)

    # orderables
    # assign field custom serializer
    # icon_list = IconSerializer(many=True)


    # assign field custom serializer field
    # related_events = RelatedEventField(many=True, read_only=True)
    related_events = EventLinkSerializer(many=True)

    # lexis_link = LexisLinkField(many=True, read_only=True)
    lexis_link = LexisLinkSerializer(many=True)

    # Stream blocks
    exploration = ExplorationField(many=True, read_only=True)
    application = ApplicationField(many=True, read_only=True)
    derivations = DerivationField(many=True, read_only=True)
    lexis_root = LexisRootField(many=True, read_only=True)
    highlight = HighlightField(many=True, read_only=True)


    class Meta:
        model = Lexis
        fields = ['id',
                  'term',
                  'part_of_speech',
                  'etymology',
                  'event_collection',
                  'icon_list',
                  'related_events',
                  'lexis_link',
                  'derivations',
                  'lexis_root',
                  'highlight',
                  'application',
                  'exploration',
                  'quotation',
                  'quotation_author',
                  'quote_source',
                  # 'quote_source_minor',
                  'star_value',
                  ]

