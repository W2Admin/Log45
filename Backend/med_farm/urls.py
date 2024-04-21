from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from med_farm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/organisation/', views.organisation_list),
    path('api/organisation/<int:id>', views.organisation_detail),
    path('api/', include('user.urls')),
]
