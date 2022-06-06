import abc

from django.conf import settings
from django.core.mail import send_mass_mail
from django.db.models import QuerySet


class NotificationServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, user: settings.AUTH_USER_MODEL, users: 'QuerySet[settings.AUTH_USER_MODEL]', subject, data):
        raise NotImplemented


class MailNotificationService(NotificationServiceInterface):

    def prepare_recipient_list(self, users: 'QuerySet[settings.AUTH_USER_MODEL]'):
        return users.values_list('email', flat=True)

    def notify(self, user: settings.AUTH_USER_MODEL, users, subject, data):
        message = (
            subject,  # subject,
            data,  # message,
            None,  # from_email,
            self.prepare_recipient_list(users)  # recipient_list
        )

        send_mass_mail([message], fail_silently=False)


class ChangedPerformedNotification:

    def __init__(self,
                 notification_service: 'NotificationServiceInterface',
                 users: 'QuerySet[settings.AUTH_USER_MODEL]',
                 subject
                 ):
        self.notification_service = notification_service
        self.users = users
        self.subject = subject

    def notify(self, user, previous_state, next_state):
        data = f"""
            Theres a changes on the next objects
            prev_state : 
                {previous_state}            
            changes:
                {next_state}

        """

        self.notification_service.notify(
            users=self.users,
            user=user,
            data=data,
            subject=self.subject
        )
