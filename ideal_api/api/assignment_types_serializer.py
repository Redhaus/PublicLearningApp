from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from events.models import EventOverview
from assignment_types.models import AssignmentTypes

# import for image link
from wagtail.images.models import Image



# observables
# Custom searializer to add custom display fields
# class EventCollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryEventCollection
#         fields = ['id', 'collection_name', 'collection_event']


# this is how you add an image link to api
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['id', 'title', 'file']


# Struct Blocks
# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class TopicsField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }



# MAIN SERIALIZER
class AssignmentTypeSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    # event_collection = EventCollectionSerializer(many=False)
    # author_image = ImageSerializer(many=False)
    topics = TopicsField(many=True, read_only=True)



    class Meta:
        model = AssignmentTypes
        fields = ['id',
                  'category_type',
                  'title',
                  'feat',
                  'verb',
                  'description',
                  'topics',


                  ]

        # lookup_field = ('author_image',)
        # lookup_field = 'author_image'

