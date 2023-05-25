from django.db import models


# Create your models here.
class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    rank = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    country = models.CharField(max_length=20)
    fav_player = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
