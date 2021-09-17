from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('',views.index,name='index'),
    path('home/',views.simple_upload,name='simple_upload'),
    #path('download/',views.simple_download,name='simple_download'),
    path('download/',views.simple_download,name='simple_download'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)