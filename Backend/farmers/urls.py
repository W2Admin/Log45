from django.urls import path
from . import views

urlpatterns = [
    path('farmers/', views.FarmerProfileListCreateView.as_view(), name='farmer-list-create'),
    path('farmers/<int:pk>/', views.FarmerProfileRetrieveUpdateDestroyView.as_view(), name='farmer-retrieve-update-destroy'),
    path('animals/', views.AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', views.AnimalRetrieveUpdateDestroyView.as_view(), name='animal-retrieve-update-destroy'),
    path('locations/', views.LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', views.LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
]
