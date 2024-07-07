from django.urls import path
from django.conf.urls.static import static
from responseApp import settings
from . import views
name_app = 'baseApp'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('allresponse/', views.allresponse, name = 'allresponse'),
    path('tovar/<int:pk>',views.TovarDetail.as_view(),name = 'tovar'),
    path('tovar_create/',views.CreateTovarCreateView.as_view(),name = 'tovar_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)