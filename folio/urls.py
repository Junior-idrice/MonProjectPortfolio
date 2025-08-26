from django.urls import path
from . import views
from personal import settings

from django.conf.urls.static import static
urlpatterns =[
    path('', views.index, name='index'),
    path('layout',views.layout, name='layout'),
    path('experience', views.experience, name='experience'),
    path('projects', views.projects, name='projects')
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)