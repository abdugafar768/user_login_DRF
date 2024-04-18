from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()

router.register('user-registrations',UserRegistration, basename = 'User')

urlpatterns = router.urls