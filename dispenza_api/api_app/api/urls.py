from django.conf.urls import url, include
from rest_framework import routers
from api_app.api import views
from api_app.api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'prodotti', views.ProdottiDispensaViewSet)
router.register(r'spese', views.SpesaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', CustomObtainAuthToken.as_view()),
]