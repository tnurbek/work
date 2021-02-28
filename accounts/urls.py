from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('images', views.ImageViewSet)
router.register('logs', views.LogViewSet)

urlpatterns = [
    path('signin', LoginView.as_view(), name='signin'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('signout', LogoutView.as_view(), name='signout'),

    path('', views.home, name='home'),
    path('fetch_images', views.fetch, name='fetch'),
    path('images/<int:pk>', views.image, name='image'),
    path('delete_image', views.delete_image, name='delete_image'),
    path('send_email', views.send_email, name='send_email'),

    path('api/v1/', include(router.urls)),
]
