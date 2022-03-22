from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.addmodel, name="addmodel"),
    re_path(r'^createmodel$', views.createmodel, name="createmodel"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
