from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from app.models import Package
from app.serializers import Package_Serializer

#Only admin can access 
class Package_List(generics.ListCreateAPIView):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = Package_Serializer
    permission_classes = [permissions.IsAdminUser]

# This class is for reading,updating and deleting (soft delete) of packages
class Package_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = Package_Serializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        package.soft_delete()
        return Response({"message": "Package is deleted but not permanently!"}, status=204)

# This class is for driver's assign package
class Assigned_Packages(generics.ListAPIView):
    serializer_class = Package_Serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Package.objects.filter(driver=self.request.user, is_deleted=False)

# Update status of the package (only accesible by drivers)
class Update_Package(generics.UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = Package_Serializer
    permission_classes = [permissions.IsAuthenticated]

# Customers can track their package location by implementing this function.
@api_view(['GET'])
def track_package(request, t_number):
    try:
        package = Package.objects.get(t_number=t_number, is_deleted=False)
        return Response({"status": package.status})
    except Package.DoesNotExist:
        return Response({"error": "Package is not found. Kindly give a valid tracking number"}, status=404)

