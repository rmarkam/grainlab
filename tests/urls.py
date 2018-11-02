from django.urls import path
from .views import TestsList, TestDetail


urlpatterns = [
    path('tests/', TestsList.as_view()),
    path('tests/<test_id>', TestDetail.as_view())
]