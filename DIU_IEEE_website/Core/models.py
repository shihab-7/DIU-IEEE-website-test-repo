from django.db import models
from Members.models import resize_image  # Reuse the resize_image helper function

# Create your models here.
class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=100, help_text="Name of the website")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload the website logo")
    about_text = models.TextField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    footer_text = models.TextField(null=True, blank=True)
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    social_media_links = models.JSONField(null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.logo:
            resize_image(self.logo.path, max_width=500, max_height=500)
        if self.background_image:
            resize_image(self.background_image.path, max_width=1920, max_height=1080)

    def __str__(self):
        return self.site_name
