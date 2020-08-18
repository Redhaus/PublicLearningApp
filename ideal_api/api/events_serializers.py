from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from events.models import EventOverview
from events.models import CategoryEventCollection

# import for image link
from wagtail.images.models import Image



# observables
# Custom searializer to add custom display fields
# class EventCollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryEventCollection
#         fields = ['id', 'collection_name', 'collection_event']


# this is how you add an image link to api
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'file']


# MAIN SERIALIZER
class EventOverviewSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    # event_collection = EventCollectionSerializer(many=False)
    author_image = ImageSerializer(many=False)

    class Meta:
        model = CategoryEventCollection
        fields = ['id',
                  'collection_event',
                  'collection_name',
                  'event_title',
                  'event_descriptor',
                  'quotation',
                  'quotation_author',
                  'quote_source',
                  # 'quote_source_major',
                  # 'quote_source_minor',z
                  'author_image',

                  ]

        # lookup_field = ('author_image',)
        # lookup_field = 'author_image'

