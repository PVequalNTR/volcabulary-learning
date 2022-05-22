from django.urls import path, include
from vols import views

urlpatterns = [
    path('latest_categories/<int:pk>/', views.latest_categories.as_view()),
    path('get_sentences/<str:string>/', views.get_sentences.as_view()),
    path('get_category/<str:name>', views.get_category.as_view()),
    path('check/<str:name>', views.check.as_view()),
]