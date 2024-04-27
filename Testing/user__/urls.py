from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('user-profiles/', views.UserProfileListCreateView.as_view(), name='user-profile-list-create'),
    path('user-profiles/<int:pk>/', views.UserProfileRetrieveUpdateDestroyView.as_view(), name='user-profile-retrieve-update-destroy'),
]
