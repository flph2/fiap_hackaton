from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from invest import views

router = routers.DefaultRouter()
router.register(r'profile', views.PerfilViewSet)
router.register(r'page-path', views.PagePathViewSet)
router.register(r'product-catalog', views.ProductCatalogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
