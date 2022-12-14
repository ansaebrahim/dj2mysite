from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank = True,upload_to = 'profile_pics')
    contact_number = models.CharField(max_length = 15)
    
    # def get_absolute_url(self):
    #     return reverse('products', kwargs={'pk': self.pk})
