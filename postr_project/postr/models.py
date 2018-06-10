from django.db import models
# Import standard auth User
from django.contrib.auth.models import User
# Import signals and receiver to autosave profile on User create or save
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    title = models.CharField(max_length=100)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    message=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    child_comments=models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    def __str__(self):
        return self.body

# Save User Profile on User create or save
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
