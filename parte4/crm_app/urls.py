from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import register
from .views import ProdutoViewSet, ClienteViewSet, VendaViewSet, EmpresaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'empresas', EmpresaViewSet)

urlpatterns = [
    path('register/', register),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
