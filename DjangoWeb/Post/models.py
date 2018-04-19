from django.db import models

# Create your models here.
from django.db import models
from Group.models import  Group
# Create your models here.

from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True)
    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse(
            "Post:all",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
