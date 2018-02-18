from django.db import models

#the basic of fields and things need in a blog


class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

