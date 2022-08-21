from myapp.models import School
from rest_framework.views import APIView
from myapp.serializer import SchoolSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SchoolList(APIView):
    def get(self, request):
        sname = School.objects.all()
        serializer = SchoolSerializer(sname, many=True)
        return Response(serializer.data)

class SchoolCreate(APIView):
    def post(self,request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):

    def get_school_pk(self, pk):
        try:
            return School.objects.get(pk=pk)
        except:
            return Response({
                'error': 'School does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        sname = self.get_school_pk(pk)
        serializer = SchoolSerializer(sname)
        return Response(serializer.data)

    def put(self, request, pk):
        sname = self.get_school_pk(pk)
        serializer = SchoolSerializer(sname, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sname = self.get_school_pk(pk)
        sname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)