from django.contrib.auth.models import User, Group
from rest_framework import serializers
from readings.models import PrimaryFocus, FurtherExplorations
from categories.models import ReadingCategory
from events.models import CategoryEventCollection

# from lexis.models import Lexis

# import for image link
from wagtail.images.models import Image
from wagtail.documents.models import Document


# from taggit.models import Tag



# observables
# Custom searializer to add custom display fields
class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEventCollection
        fields = ['id', 'collection_name', 'collection_event']


# observables
# Custom searializer to add custom display fields
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrimaryFocusTag
#         fields = ['id', 'content_object_id', 'tag_id']


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ['name', 'id']



#
# class TagField(serializers.RelatedField):
#
#     # uses existing data to refetch data needed
#     # fetch tag name and id based on tag.id
#     def to_representation(self, value):
#         tag = Tag.objects.get(id=value.id)
#
#         # returns new model data in format you want
#         return {
#             "id": tag.id,
#             "term": tag.name,
#             # "part_of_speech": term.part_of_speech
#         }



# READ ONLY to Display custom format data
# reformat data presentation of blocks to get id and value
class KeywordsField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "value": value.value,
        }


# Field Serializers
# this is how you add an image link to api
class ReadingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingCategory
        fields = ['id', 'category_name']


# this is how you add an image link to api
class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'file']

# this is how you add an image link to api
class ResourceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file']




# MAIN SERIALIZER PRIMARY FOCUS
class PrimaryFocusSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)

    event_collection = EventCollectionSerializer(many=False)
    keywords = KeywordsField(many=True, read_only=True)
    reading_category = ReadingCategorySerializer(many=False)
    book_image = BookImageSerializer(many=False)


    class Meta:
        model = PrimaryFocus
        fields = ['id',
                  'event_collection',
                  'title_major',
                  'synopsis',
                  'level_ability',
                  'page_count',
                  'reading_category',
                  'book_image',
                  'author_first_name',
                  'author_last_name',
                  'author_dob',
                  'keywords',
                  'purchase_link',
                  'source',
                  ]





# MAIN SERIALIZER FURTHER_EXPLORATIONS
class FurtherExplorationsSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)

    # tags = TagSerializer(many=True)
    event_collection = EventCollectionSerializer(many=False)
    keywords = KeywordsField(many=True, read_only=True)
    reading_category = ReadingCategorySerializer(many=False)
    resource_link = ResourceLinkSerializer(many=False)



    class Meta:
        model = FurtherExplorations
        fields = ['id',
                  'event_collection',
                  'title_minor',
                  'excerpt',
                  'reading_category',
                  'resource_link',
                  'author_first_name',
                  'author_last_name',
                  'author_dob',
                  'keywords',
                  ]

