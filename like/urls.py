from django.urls import path

from like import views

urlpatterns = [
    path('', views.LikeCreateView.as_view()),
    path('delete/', views.LikeDeleteView.as_view())
]
