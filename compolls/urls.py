from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'compolls'
urlpatterns = [
    path('', views.compoll_question, name='community_poll_question'),
    path('ajax/manage_vote', views.manage_vote, name='manage_vote'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
