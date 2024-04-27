from django.urls import path
from . import views

urlpatterns = [
    path('organisations/', views.OrganisationListCreateView.as_view(), name='organisation-list-create'),
    path('organisations/<int:pk>/', views.OrganisationRetrieveUpdateDestroyView.as_view(), name='organisation-retrieve-update-destroy'),
]
