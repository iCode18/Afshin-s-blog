# use separated url file to have clean and more manageable
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# last line make it possible to render pictures
urlpatterns = [
    path('', views.home, name='home'),
    url(r'posts/(?P<post_id>\d+)/$', views.post_details, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
