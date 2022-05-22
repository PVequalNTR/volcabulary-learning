from django.urls import path, include
from vols import views

urlpatterns = [
    path('latest_categories/<int:pk>/', views.latest_categories.as_view()),
    path('get_sentences/<int:id>/', views.get_sentences.as_view()),
    path('get_category/<str:name>', views.get_category.as_view()),
]