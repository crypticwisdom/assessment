import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     slug = models.SlugField(default=uuid.uuid4, null=False, blank=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.user)



