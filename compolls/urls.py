from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'compolls'
urlpatterns = [
    path('', views.community_poll_view, name='community_poll_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
