from django.urls import path
from . import views

urlpatterns = [
    path('farmers/', views.FarmerListCreateView.as_view(), name='farmer-list-create'),
    path('farmers/<int:pk>/', views.FarmerRetrieveUpdateDestroyView.as_view(), name='farmer-retrieve-update-destroy'),
]
