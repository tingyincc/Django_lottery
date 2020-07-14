from django.urls import path

from . import views

app_name = 'lottery'
urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.simple_upload, name='import'),
    path('<int:award_id>/reset/', views.resetAward, name='reset'),
    path('<int:award_id>/doLottery/', views.doLottery, name='doLottery'),
    path('reload/', views.reloadPage, name='reload'),
]