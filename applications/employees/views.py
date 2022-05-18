from rest_framework import mixins, viewsets, permissions
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

    # def get_permissions(self):
    #     """
    #        Instantiates and returns the list of permissions that this view requires.
    #     """
    #     permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]
