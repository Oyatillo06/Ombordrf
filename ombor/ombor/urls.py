
from django.contrib import admin
from django.urls import path, include
from app1.views import ProductViewSet,ClientViewSet,StatsViewSet,OmborViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
r=DefaultRouter()
r.register('product',ProductViewSet)
r.register("client",ClientViewSet)
r.register("stats",StatsViewSet)
r.register("ombor",OmborViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(r.urls)),
    path('get-token/',TokenObtainPairView.as_view()),
    path('token-refresh/',TokenRefreshView.as_view()),


]
