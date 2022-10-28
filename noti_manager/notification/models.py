from django.db import models

project_type_choice = (
    ('organization', 'organization'), ('individual','individual')
)

# class models.Model(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=20, choices=project_type_choice)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    reserved_at = models.DateTimeField()
    status = models.CharField(max_length=20,  choices=(('success', 'success'), ('fail', 'fail')))
    type = models.CharField(max_length=20, choices=project_type_choice)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TargetUser(models.Model):
    username = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationTargetUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_user = models.ForeignKey(TargetUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    notification = models.ForeignKey(Notification, related_name='NotiReservation', on_delete=models.CASCADE)
    reserved_at = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationLog(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    target = models.ForeignKey('TargetUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(('success', 'success'), ('fail', 'fail'), ('sending', 'sending')))
    request = models.JSONField(null=True)
    response = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MessageTemplate(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
