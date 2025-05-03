from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Helper function for resizing images
def resize_image(image_path, max_width, max_height):
    img = Image.open(image_path)
    if img.height > max_height or img.width > max_width:
        output_size = (max_width, max_height)
        img.thumbnail(output_size)
        img.save(image_path)

class MemberProfile(models.Model):
    MEMBER_TYPE_CHOICES = [
        ('advisor', 'Advisor'),
        ('committee', 'Committee'),
        ('general', 'General Member'),
        ('alumni', 'Alumni'),
        ('executive', 'Executive'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, default="No information provided.")
    skills = models.TextField(blank=True, default="No skills listed.")
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    member_type = models.CharField(max_length=50, choices=MEMBER_TYPE_CHOICES, default='general')
    member_id = models.CharField(max_length=50, unique=True, blank=True)
    club_position = models.CharField(max_length=100, blank=True, default="Member")
    joined_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.member_id:
            last_member = MemberProfile.objects.filter(member_id__startswith="IEEE-").order_by('id').last()
            if last_member:
                last_id = int(last_member.member_id.split("-")[1])
                self.member_id = f"IEEE-{last_id + 1:03d}"
            else:
                self.member_id = "IEEE-001"
        super(MemberProfile, self).save(*args, **kwargs)

        if self.profile_picture:
            resize_image(self.profile_picture.path, 400, 400)

    def __str__(self):
        return self.user.username


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Projects, self).save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path, 500, 500)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

