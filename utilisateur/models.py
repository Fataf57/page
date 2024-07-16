from django.db import models
from django.contrib.auth.models import User
import os 

def renomer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(intance.user.username, ext)
    return os.path.join(upload_to, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio =models.CharField(max_length=50, blank=True)
    photo_profile = models.ImageField(upload_to=renomer_image, blank=True)

    eleve = 'eleve'
    enseignant = 'enseignant'
    parent = 'parent'

    type_user = [
        (eleve, 'eleve'),(enseignant, 'enseignant'),(parent, 'parent')
    ]

    type_profile = models.CharField(max_length=100, choices=type_user, default=eleve)
    
    def __str__(self):
        return self.user.username