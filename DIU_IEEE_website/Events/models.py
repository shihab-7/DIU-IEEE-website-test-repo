from django.db import models
from Members.models import resize_image

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path, max_width=1600, max_height=600)

    def __str__(self):
        return f"{self.title} on {self.event_date.strftime('%Y-%m-%d')}"
