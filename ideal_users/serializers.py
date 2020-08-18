from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.registration.views import RegisterView
from rest_framework import serializers



# TEACHERS REGISTRATION REST API //////////////////////
# ENDPOINT: /rest-auth/registration/teacher/

# Grade level choices
LEVEL = (
    ('K-5', 'K-5'),
    ('6-8', '6-8'),
    ('9-12', '9-12'),
    ('K-12', 'K-12'),
    ('K-8', 'K-8'),
    ('6-12', '6-12')
)


# set up custom fields, and pass them to user so they can be used in signal to create
# teacher profile and set the users role as a Teacher
class TeacherRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    grade_level = serializers.ChoiceField(LEVEL)

    def custom_signup(self, request, user):
        user.role = "teacher"
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.grade_level = self.validated_data.get('grade_level', '')
        user.save(update_fields=['first_name', 'last_name'])

class TeacherRegistrationView(RegisterView):
    serializer_class = TeacherRegistrationSerializer



# SCHOOL REGISTRATION REST API //////////////////////
# ENDPOINT: /rest-auth/registration/school/
SCHOOL_LEVEL = (
    ('primary', 'primary'),
    ('secondary', 'secondary'),
    ('high school', 'high school')
)


class SchoolRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    school_level = serializers.ChoiceField(SCHOOL_LEVEL)
    school_name = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.role = "school"
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.school_level = self.validated_data.get('school_level', '')
        user.school_name = self.validated_data.get('school_name', '')
        user.save(update_fields=['first_name', 'last_name'])

class SchoolRegistrationView(RegisterView):
    serializer_class = SchoolRegistrationSerializer




# SCHOOL REGISTRATION REST API //////////////////////
# ENDPOINT: /rest-auth/registration/editor/
class EditorRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.role = "editor"
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])


class EditorRegistrationView(RegisterView):
    serializer_class = EditorRegistrationSerializer

