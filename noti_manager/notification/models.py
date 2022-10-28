from django.db import models


project_type_choice = (
    'organization', 'individual',
)

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimeStampedModel):
    email = models.EmailField()
    password = models.CharField(max_length=256)


class Project(TimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=20, choices=project_type_choice)


class Notification(TimeStampedModel):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    reserved_at = models.DateTimeField()
    status = models.CharField(choices=('success', 'fail'))
    type = models.CharField(choices=project_type_choice)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class TargetUser(TimeStampedModel):
    username = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    data = models.JSONField()


class NotificationTargetUser(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_user = models.ForeignKey(TargetUser, on_delete=models.CASCADE)


class Reservation(TimeStampedModel):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField()
    status = models.CharField(max_length=20)


class NotificationLog(TimeStampedModel):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    target = models.ForeignKey('TargetUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=('success', 'fail', 'sending',))
    request = models.JSONField(null=True)
    response = models.JSONField(null=True)


class Message(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)


class MessageTemplate(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
