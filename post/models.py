import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default=uuid.uuid4, null=False, blank=False)
    title = models.CharField(max_length=40, null=True)
    content = models.TextField()
    likes_count = models.PositiveBigIntegerField(null=True, default=0)
    likes = models.ManyToManyField(User, related_name='liked_by', blank=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} - {self.slug}"

    def add_likes_count(self):
        self.likes_count = self.likes.count()
        self.save()
        return str(self.likes_count)
