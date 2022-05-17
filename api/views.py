from rest_framework.response import Response
from rest_framework.decorators import api_view

from applications.employees.serializers import EmployeeSerializer


@api_view(['GET'])
def api_home(request):

    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        print(serializer.data)

        return Response(serializer.data)

    return Response({'invalid': 'Not good data'}, status=400)
