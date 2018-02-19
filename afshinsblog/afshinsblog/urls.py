from django.contrib import admin
from django.urls import path, include

# use include to pack each urls into own app url file
urlpatterns = [
    path('malekomodir/', admin.site.urls),
    path('', include('posts.urls')),
]
