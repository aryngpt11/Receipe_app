from django.db import models
from django.contrib.auth.models import User


class Reciepe(models.Model):
    user=models.ForeignKey(User ,on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe")
    receipe_views_count=models.IntegerField(default=1)
    