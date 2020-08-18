# a custom view hooked into a custom url
# INVITATION VIEW TO ACCEPT MULTIPLE LINK CLICKS

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.dispatch import receiver

from invitations.views import AcceptInvite
from invitations.app_settings import app_settings
from invitations.adapters import get_invitations_adapter
from invitations.models import Invitation
from invitations.signals import invite_accepted

from allauth.account.signals import user_signed_up
from allauth.account.models import EmailAddress

# this view overwrites invite view that allows link to be clicked twice
class AcceptInviteView(AcceptInvite):
    def post(self, *args, **kwargs):
        self.object = invitation = self.get_object()

        # Compatibility with older versions: return an HTTP 410 GONE if there
        # is an error. # Error conditions are: no key, expired key or
        # previously accepted key.
        if app_settings.GONE_ON_ACCEPT_ERROR and \
                (not invitation or
                 (invitation and (invitation.accepted or
                                  invitation.key_expired()))):
            return HttpResponse(status=410)

        # No invitation was found.
        if not invitation:
            # Newer behavior: show an error message and redirect.
            get_invitations_adapter().add_message(
                self.request,
                messages.ERROR,
                'invitations/messages/invite_invalid.txt')
            return redirect(app_settings.LOGIN_REDIRECT)

        # The invitation was previously accepted, redirect to the login
        # view.
        if invitation.accepted:
            get_invitations_adapter().add_message(
                self.request,
                messages.ERROR,
                'invitations/messages/invite_already_accepted.txt',
                {'email': invitation.email})
            # Redirect to login since there's hopefully an account already.
            return redirect(app_settings.LOGIN_REDIRECT)

        # The key was expired.
        if invitation.key_expired():
            get_invitations_adapter().add_message(
                self.request,
                messages.ERROR,
                'invitations/messages/invite_expired.txt',
                {'email': invitation.email})
            # Redirect to sign-up since they might be able to register anyway.
            return redirect(app_settings.SIGNUP_REDIRECT)

        get_invitations_adapter().stash_verified_email(
            self.request, invitation.email)

        get_invitations_adapter().add_message(
            self.request,
            messages.SUCCESS,
            'invitations/messages/invite_accepted.txt',
            {'email': invitation.email})

        return redirect(app_settings.SIGNUP_REDIRECT)


@receiver(user_signed_up)
def accept_invite(sender, request, user, **kwargs):
    # Traverse from the user to verified email addresses. It is possible for a
    # user to already have multiple email addresses if they typed in a different
    # email after accepted the invite. In this case, the user will have two
    # emails, but only one will be verified.
    addresses = EmailAddress.objects.filter(user=user, verified=True) \
                                    .values_list('email', flat=True)
    # Check if any invites exist for this address and were accepted.
    invites = Invitation.objects.filter(email__in=addresses)
    if invites:
        # Mark all these invites as accepted.
        invites.update(accepted=True)
        for invite in invites:
            # Note that this doesn't send it with a request.
            invite_accepted.send(sender=Invitation, email=invite.email)

        # Figure out if you care if there are multiple invites here.