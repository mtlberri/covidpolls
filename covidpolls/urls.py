from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'covidpolls'
urlpatterns = [
    path('', views.get_parent_preferences, name='get_parent_preferences'),
    path('thanks/', views.thanks, name='thanks'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
