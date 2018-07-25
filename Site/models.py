from django.db import models

# from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.
class Member(models.Model):
    firstName    = models.Charfield(max_length=20)
    lastName     = models.CharField(max_length=20)
    profilePhoto = models.ImageField(upload_to="members")
    userName     = models.TextField(max_length=25)
    contact      = models.IntegerField(default=None)
    email        = models
    # def validate_number(contact):
    #         if not len(contact) == 10:
    #              raise ValidationError("%s Incorrect contact prototype" %contact)



class Posts(models.Model):
    member       = models.ForeignKey(Member, on_delete=models.CASCADE)
    postTitle    = models.CharField(max_length=100)
    postContent  = models.TextField(max_length=1000)
    pubDate      = models.DateTimeField(auto_now_add=True, blank=True)


class PostsImages(models.Model):
    def __str__(self):
        return str(self.image).split('/')[-1]
    post         = models.ForeignKey(Posts)
    # image        = models.ImageField(upload_to=post_file_name,default='post_images/'+str(id)+'.jpg')


class Events(models.Model):
    eventName    = models.CharField(max_length=20)
    eventDate    = models.DateField(null=True, blank=True)
    eventRegDate = models.DateField(null=True, blank=True)
    eventContent = models.TextField(null=True, blank=True)

