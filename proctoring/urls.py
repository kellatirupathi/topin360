from django.urls import path, re_path
from . import views

app_name = 'proctoring'

urlpatterns = [
    path('', views.home, name='Home'),
    # path('proctor=<slug:proctor_id>/user_id=<slug:user_id>&assessment_id=<slug:assessment_id>',
    #      views.proctor, name='Proctor'),
    path('proctor=<slug:proctor_id>', views.proctor, name='Proctor'),
    re_path(r'^media/videos/.*$', views.download_file, name='DownloadMp4'),
]
