from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.task import task_send_email
from apps.views import UserViewSet, RegisterCreateAPIView, ProductListAPIView, ProductRetrieveUpdateDestroyAPIView


def send_email_task(req):
    task_send_email().delay('xabar', 'jjj', ['sokidjonovabdulbosit53@gmail.com'])
    return JsonResponse({'success': True})


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register', RegisterCreateAPIView.as_view(), name='category'),
    path('products', ProductListAPIView.as_view(), name='products'),
    path('products/upd_del',ProductRetrieveUpdateDestroyAPIView.as_view(), name='products_update')

]
