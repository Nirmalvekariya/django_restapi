from django.urls import path, include
from .import views
from rest_framework import routers

app_name = "languages"

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)


urlpatterns = [
    path('', include(router.urls))
]