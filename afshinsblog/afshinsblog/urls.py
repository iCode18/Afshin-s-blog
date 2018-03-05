from django.contrib import admin
from django.urls import path, include
import sitepages.views
# use include to pack each urls into own app url file
urlpatterns = [
    path('malekomodir/', admin.site.urls),
    path('', include('posts.urls')),
    path('about/', sitepages.views.about,name='about'),
    path('posts/(?P<post_id>\d+)/', include('posts.urls')),
]
