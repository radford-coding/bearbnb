from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('caves/', views.CaveIndex.as_view(), name='cave-index'),
    path('caves/<int:pk>/', views.CaveDetail.as_view(), name='cave-detail'),
    path('caves/create/', views.CaveCreate.as_view(), name='cave-create'),
]
