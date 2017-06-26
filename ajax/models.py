from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    like = models.IntegerField(default=50)
    # liking = models.ForeignKey(C)
    def __str__(self):
        return self.user.username

class C(models.Model):
    author = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=20)
    like = models.IntegerField(default=0)
    liking = models.ManyToManyField(User, null=True, blank=True)
