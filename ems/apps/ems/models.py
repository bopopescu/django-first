from django.db import models
from django import forms

import datetime
# from django.contrib.auth.models import AbstractBaseUser


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    ip_address = models.CharField(
        max_length=20, blank=False, unique=True, null=False)


# class Notification(models.Model):

#     name = models.CharField(max_length=255, blank=False, null=False)
#     # event or alarm
#     unit = models.BooleanField(
#         blank=False, null=False, default=0)  # 0=alarm, 1=event
#     message = models.CharField(max_length=255, blank=False, null=False)
#     created_on = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    of_type = models.BooleanField(
        default=0, null=False, blank=False)  # 0 = alarm, 1 = event
    severity_level = models.CharField(max_length=10, blank=True, null=True)
    notification = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=0)
    created_on = models.DateTimeField(
        default=datetime.datetime.now, blank=False)
    updated_on = models.DateTimeField(
        default=datetime.datetime.now, blank=False)

    def __unicode__(self):
        return "Event: "+self.notification if self.of_type else "Alarm: "+self.notification

    def __str__(self):
        return self.notification


class Site(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    owner = models.CharField(max_length=255, blank=False, null=False)
    nms_ip = models.CharField(max_length=20, blank=False, null=False)
    is_master = models.BooleanField(default=1, blank=False, null=False)
    master_ip = models.CharField(max_length=20, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Slave(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    ip_address = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Syncup(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Interface(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Element(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=255,  blank=False, null=False)
    configuration = models.TextField(default="{}", blank=False, null=False)
    interface = models.ForeignKey(
        to=Interface, on_delete=models.CASCADE, related_name='elements')
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class State(models.Model):

    element = models.ForeignKey(
        to=Element, related_name='statuses', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Temperature(models.Model):
    temperature = models.FloatField(blank=False, null=False, default=0)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.temperature


class CDR(models.Model):
    caller_id = models.CharField(max_length=100, blank=False, null=False)
    callee_id = models.CharField(max_length=100, blank=False, null=False)
    start_call_at = models.DateTimeField(auto_now_add=True)
    end_call_at = models.DateTimeField(
        auto_now_add=False, default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)


class Group(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

# class User(AbstractBaseUser):
#     username = None
#     email = models.CharField(max_length=20, unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # middle_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # username = models.CharField(
    #     max_length=50, blank=False, null=False, unique=True)
    # password = models.CharField(max_length=100, blank=False, null=False)

    # def __unicode__(self):
    #     return self.first_name + ' ' + self.last_name


class User(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(
        max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=0, blank=False, null=False)
    last_login = models.DateTimeField(auto_now_add=True)

    def is_authenticated(self):
        return True

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


    def set_password(self, password):
        self.password = password
        if settings.USE_ENCRYPTED_PASSWORD:
            from hashlib import sha256
            self.password = sha256(password)


class Permission(models.Model):
    name = models.CharField(max_length=50)
    permission = models.CharField(max_length=50)

    group = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.name


# class ElementForm(forms.Form):
#     class Meta:
#         model = Element

#     subject = forms.CharField(label='New label')


class Help(models.Model):
    title = models.CharField(max_length=255, blank=None)
    description = models.TextField(blank=False, null=False)
