# get user and group models
from django.contrib.auth.models import Group

# listen for signup allauth signal
from allauth.account.signals import user_signed_up

# get reciever to dispatch signal
from django.dispatch import receiver

# import profiles for teacher and school
from teacher_profile.models import TeacherProfile
from school_profile.models import SchoolProfile
from invitations.models import Invitation



# Signals fired once user signed up
@receiver(user_signed_up)
def add_token(request, user,  **kwargs):

    # request and user and both available
    # request.user return anonuser, for data is on user object
    print("USER: ", user)


    # If invite by school get invite object and below assign a those teachers to those schools
    invite = Invitation.objects.filter(email=user.email).first()
    print('INVITE: ', invite)

    if invite:

        # get group and assign it
        group = Group.objects.get(name='Teacher')
        user.groups.add(group)

        wholename = user.first_name + ' ' + user.last_name

        # get inviter_id
        schoolAdminID = invite.inviter_id
        print('INVITE_ID_INSIDE: ', schoolAdminID)

        # get school obj with inviter schooladmin_id
        parentSchoolObj = SchoolProfile.objects.filter(primary_contact_id=schoolAdminID).first()

        # create teacher profile
        profile = TeacherProfile.objects.create(
            user=user,
            full_name=wholename,
            school_name=parentSchoolObj,
        )

        return profile




    # Check for teacher API Call and assign user to teacher group and create teacher profile /////////////////////////////
    if(user.role == "teacher"):

        group = Group.objects.get(name='Teacher')
        user.groups.add(group)

        wholename = user.first_name + ' ' + user.last_name

        profile = TeacherProfile.objects.create(
            user=user,
            full_name=wholename
        )

        return profile


    # if user role is school assign to school group and make school profile /////////////////////////////
    if (user.role == "school"):

        group = Group.objects.get(name='School')
        user.groups.add(group)

        profile = SchoolProfile.objects.create(
            primary_contact=user,
            school_name=user.school_name
        )

        return profile



    # if editor role create user and assign to editors group /////////////////////////////
    if (user.role == "editor"):

        group = Group.objects.get(name='Editors')
        user.groups.add(group)


