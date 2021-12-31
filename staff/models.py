from django.db import models
from django.utils import timezone
from django.conf import settings


"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    crated_date = models.DateTimeField(default=timezone.now)
    post_is_ready = 'R'
    post_not_ready = 'NR'
    STATUS = [
        (post_is_ready, 'Ready'),
        (post_not_ready, 'Not Ready'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=post_not_ready,
        )

    def publish(self):
        self.status = "R"
        self.save()

    def __str__(self):
        return self.title
"""
