from django.urls import path
from .views import createShortUrlView, redirectView

urlpatterns = [
    path('', createShortUrlView),
    path('<str:shortUrl>', redirectView)
]