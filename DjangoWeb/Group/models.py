from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# from accounts.models import User

#import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()
# Create your models here.

class Group(models.Model):


    name = models.CharField(max_length=255, unique=True)

    description = models.TextField(blank=True)
    #description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group_detail",kwargs={'pk':self.pk})

    class Meta:
        ordering = ["name"]

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='membership')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.User.username
    class Meta:
        unique_together = ("group", "user")
