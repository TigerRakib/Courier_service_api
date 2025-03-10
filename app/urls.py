from django.urls import path
from app.views import Package_List, Package_Details, Assigned_Packages, Update_Package, track_package

urlpatterns = [
    path('packages/', Package_List.as_view(), name='all_packages'),
    path('packages/<int:pk>/', Package_Details.as_view(), name='package_details'),
    path('assigned_packages/', Assigned_Packages.as_view(), name='assigned_packages'),
    path('update_status/<int:pk>/', Update_Package.as_view(), name='update'),
    path('track/<str:t_number>/', track_package, name='track'),
]
