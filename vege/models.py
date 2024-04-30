from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class recipe(models.Model):
    User=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name=models.TextField()
    recipe_description=models.TextField()
    # recipe_img=models.ImageField(upload_to="images/")
    recipe_img=models.ImageField(upload_to='images/', storage=RawMediaCloudinaryStorage())
    