from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import *

router = DefaultRouter()
router.register(r"author", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"loans", LoanViewSet)

urlpatterns = [path("", include(router.urls))]
