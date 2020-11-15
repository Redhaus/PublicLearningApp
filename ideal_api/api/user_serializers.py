from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from events.models import EventOverview
from teacher_profile.models import TeacherProfile
from school_profile.models import SchoolProfile


# import for image link
from wagtail.images.models import Image

from django.contrib.auth.models import User


# this is how you add an image link to api
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'file']


# this is how you add an image link to api
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'username',
                  'password',
                  'first_name',
                  'last_name',
                  'groups',
                  'user_permissions',
                  'is_staff',
                  'is_active'
                  ]

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolProfile
        fields = ['id', 'school_name']


# MAIN SERIALIZER
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    # display string of event term belongs to
    # standard_type = serializers.StringRelatedField(many=False)
    # event_collection = EventCollectionSerializer(many=False)
    profile_image = ImageSerializer(many=False)
    user = UserSerializer(many=False)
    school_name = SchoolSerializer(many=False)

    def update(self, instance, validated_data):
        # instance.name = validated_data.get('name', instance.name)

        # get user Data if it exists in update request
        if "user" in validated_data:
            # get user instance
            user = instance.user
            # get all update data
            userData = validated_data["user"]

            # check if specific user data exists in request, if so assign to user
            if 'first_name' in userData:
                user.first_name = userData['first_name']
            if 'last_name' in userData:
                user.last_name = userData['last_name']
            if 'email' in userData:
                user.email = userData['email']

            # save user
            user.save()

        # check for profile data, if exists assign to profile instance
        if "teacher_bio" in validated_data:
            instance.teacher_bio = validated_data["teacher_bio"]

        if "grade_level" in validated_data:
            instance.grade_level = validated_data["grade_level"]

        # save instance and return it
        instance.save()
        return instance




    class Meta:
        model = TeacherProfile
        fields = ['id',
                  'user',
                  'full_name',
                  'teacher_bio',
                  'subjects',
                  'school_name',
                  'grade_level',
                  'profile_image',

                  ]

        # lookup_field = ('author_image',)
        # lookup_field = 'author_image'

