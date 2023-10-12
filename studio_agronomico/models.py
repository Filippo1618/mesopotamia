from django.db import models
from django.contrib.auth.admin import User 
from django.contrib import admin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.admin import UserAdmin

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    age = models.IntegerField(null = True, blank = True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    followed_blogposts = models.ManyToManyField('BlogPost', blank=True)


    def __str__(self):
        return self.nickname or "error"

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class BlogPost(models.Model):

    TYPE_CHOICES = [
        ("news", "News"),
        ("bando", "Bando"),
        ("altro", "Altro"),
    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    desc = models.TextField(max_length=2500, blank=False, null=False)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="altro", null= False)
    value = models.IntegerField(null=False, blank=False)
    new = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True, blank=True )
    ref_link = models.CharField(max_length=150, blank=True, null=True)

    # Nuovo campo per tenere traccia dei follower
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return f"{self.title}, {self.value}, {self.desc}" or "error"
    
# Define an inline for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Extend the UserAdmin class
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )  # Add UserProfileInline to the inlines list

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
