from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from rest_framework import serializers


#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#
#     # def create(self, *args, **kwargs):
#     #     user = super().create(*args, **kwargs)
#     #     p = user.password
#     #     user.set_password(p)
#     #     user.save()
#     #     return user
#
#     def update(self, instance, validated_data):
#         user = instance
#         # p = user.password
#         # user.set_password(p)
#         # user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = "__all__"


#
# WORKING
class UserSerializer(serializers.ModelSerializer):

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    # function to check if old pw is valid
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
            # _({'message': "Your old password was entered incorrectly. Please enter it again."})
            _("Your old password was entered incorrectly. Please enter it again.")

            )
        return True

    # function to check if both pw match
    def validate_new_password(self, data):
        if data['password_01'] != data['password_02']:
            # raise serializers.ValidationError(_({'message': "The two password fields didn't match."}))
            raise serializers.ValidationError(_("The two password fields didn't match."))

        return True

    # custom update function to update password
    def update(self, *args, **kwargs):

        # get user and request data
        user = super().update(*args, **kwargs)
        request = self.context.get("request")
        data = request.data

        # assign vars from data
        old_password = data['old_password']
        password_01 = data['password_01']

        # check validation of user input data old and new passwords
        validate_old = self.validate_old_password(old_password)
        validate_new = self.validate_new_password(data)

        # if old and new pass validation then update password
        if validate_old & validate_new:
            user.set_password(password_01)
            user.save()
            return user




    class Meta:
        model = User
        fields = "__all__"

# --------------------------


# Confirm check
#
#
# old_password = serializers.CharField(max_length=128, write_only=True, required=True)
#   new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
#   new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)
#
#   def validate_old_password(self, value):
#       user = self.context['request'].user
#       if not user.check_password(value):
#           raise serializers.ValidationError(
#               _('Your old password was entered incorrectly. Please enter it again.')
#           )
#       return value
#
#   def validate(self, data):
#       if data['new_password1'] != data['new_password2']:
#           raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
#       password_validation.validate_password(data['new_password1'], self.context['request'].user)
#       return data
#
#   def save(self, **kwargs):
#       password = self.validated_data['new_password1']
#       user = self.context['request'].user
#       user.set_password(password)
#       user.save()
#       return user
