from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'covidpolls'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_form_in_db/', views.save_form_in_db, name='save_form_in_db'),
    path('<str:child_name>/confirmation/', views.confirmation, name='confirmation'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
