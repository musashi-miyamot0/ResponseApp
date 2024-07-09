from django.urls import path
from django.conf.urls.static import static
from responseApp import settings
from . import views
name_app = 'baseApp'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tovar/<int:pk>',views.TovarDetail.as_view(),name = 'tovar'),
    path('tovar_create/',views.CreateTovarCreateView.as_view(),name = 'tovar_create'),
    path('tags/<int:pk>', views.GetTags.as_view(), name='get_tags'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)