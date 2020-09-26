from rest_framework import serializers
from categories.models import ReadingCategory, ContinualGoalStandardType, ExtensionCommandType

# MAIN SERIALIZER
class ReadingCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ReadingCategory
        fields = ['id',
                  'category_name'
                  ]


class GoalStandardTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ContinualGoalStandardType
        fields = ['id',
                  'standard_type'
                  ]

class ExCommandTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExtensionCommandType
        fields = ['id',
                  'command_name'
                  ]