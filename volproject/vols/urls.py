from django.urls import path, include
from vols import views

urlpatterns = [
    path('latest_categories/<int:pk>/', views.latest_categories.as_view()),
    path('get_sentences/<int:id>/', views.get_sentences.as_view()),
    path('get_category/<int:id>', views.get_category.as_view()),
    path('check/<str:name>', views.check.as_view()),
    path('add_category', views.add_category.as_view()),
]