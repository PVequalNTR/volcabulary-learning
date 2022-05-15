from django.urls import path, include
from vols import views

urlpatterns = [
    path('latest_categories/<int:pk>/', views.latest_categories.as_view()),
    path('sentence/<str:s>/', views.sentence.as_view()),
]