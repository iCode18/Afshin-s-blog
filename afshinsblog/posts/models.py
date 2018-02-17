from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()


