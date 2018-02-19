from django.db import models

# the basic of fields and things need in a blog


class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    # to make it more understandable
    def __str__(self):
        return self.title

    # to show more proper date format
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # short body if it is long
    def summary(self):
        return self.body[:100]