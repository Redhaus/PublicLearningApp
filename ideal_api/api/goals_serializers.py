from django.contrib.auth.models import User, Group
from rest_framework import serializers
from continual_goals.models import ContinualGoals
from categories.models import ContinualGoalStandardType


# observables
# Custom searializer to add custom display fields
class StandardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinualGoalStandardType
        fields = ['standard_type', 'id']



# MAIN SERIALIZER
class ContinualGoalSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    standard_type = StandardTypeSerializer(many=False)


    class Meta:
        model = ContinualGoals
        fields = ['id',
                  'goal',
                  'explanation',
                  'video_link',
                  'standard_type',
                  ]
