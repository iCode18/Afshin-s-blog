from django.contrib import admin
from .models import Post

# get Post DB visible under the admin portal
admin.site.register(Post)
