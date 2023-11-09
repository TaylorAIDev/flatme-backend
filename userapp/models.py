from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Flatmate(models.Model):
    id = models.AutoField(primary_key=True)
    auth = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    kind = models.CharField(max_length=100, default=None, null=True)
    roomsize = models.CharField(max_length=100, default=None, null=True)
    rent = models.CharField(max_length=100, default=None, null=True)
    available = models.CharField(max_length=100, default=None, null=True)
    suitable = models.CharField(max_length=100, default=None, null=True)
    flat = models.CharField(max_length=100, default=None, null=True)
    provided = models.CharField(max_length=100, default=None, null=True)
    roomIncluded = models.CharField(max_length=100, default=None, null=True)
    photo = models.CharField(max_length=100, default=None, null=True)
    description = models.CharField(max_length=100, default=None, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE,default=None, null=True)
    name = models.CharField(max_length=100, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    getStart = models.CharField(max_length=100, default=None, null=True)
    describeItem = models.CharField(max_length=100, default=None, null=True)
    country = models.CharField(max_length=100, default=None, null=True)
    living = models.CharField(max_length=100, default=None, null=True)
    address = models.CharField(max_length=100, default=None, null=True)
    size = models.CharField(max_length=100, default=None, null=True)
    preparePay = models.IntegerField(default=None, null=True)
    kind = models.CharField(max_length=100, default=None, null=True)
    room_size = models.CharField(max_length=100, default=None, null=True)
    move_date = models.CharField(max_length=100, default=None, null=True)
    coming = models.CharField(max_length=100, default=None, null=True)
    description = models.CharField(max_length=100, default=None, null=True)
    def __str__(self):
        return self.name

class ImageModel(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE,default=None, null=True)
    name = models.CharField(max_length=100, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    room_image_field= models.ImageField(upload_to='roomImage/', default=None, null=True)
    user_image_field= models.ImageField(upload_to='userImage/', default=None, null=True)
    room_file_path = models.CharField(max_length=255, default=None, null=True)
    user_file_path = models.CharField(max_length=255, default=None, null=True)
    def __str__(self):
        return self.name

class SavedRooms(models.Model):
    name = models.CharField(max_length=100, default=None, null=True)
    cost = models.IntegerField(default=None, null=True)
    kind = models.CharField(max_length=100, default=None, null=True)
    room_size = models.CharField(max_length=100, default=None, null=True)
    def __str__(self):
        return self.name