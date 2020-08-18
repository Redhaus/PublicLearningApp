from django.contrib.auth.models import User, Group
from rest_framework import serializers
from key_questions.models import KeyQuestions
from events.models import CategoryEventCollection



# observables
# Custom searializer to add custom display fields
class EventCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEventCollection
        fields = ['id', 'collection_name', 'collection_event']



# MAIN SERIALIZER
class KeyQuestionsSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    event_collection = EventCollectionSerializer(many=False)
    # questions = QuestionSerializer(many=True)

    class Meta:
        model = KeyQuestions
        fields = ['id',
                  'question',
                  'explanation',
                  'video_link',
                  'event_collection',

                  ]
