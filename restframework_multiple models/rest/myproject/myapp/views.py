from django.shortcuts import render
from myapp.models import empmodel, cricketmodel
from myapp.serializers import EmpSerializer,cricketSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
# employee model
class empmodels1API(APIView):
    def get(self, request):
        empobj = empmodel.objects.all() 
        empserializerobj = EmpSerializer(empobj,many=True) 
        # resultmodel = empserializerobj.data+cricketserializerobj.data
        return Response(empserializerobj.data)

class EmpCreate(APIView):
    def post(self, request):
        serializer1 = EmpSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class empDetail(APIView):

    def get_emp_pk(self, pk):
        try:
            return empmodel.objects.get(pk=pk)
        except:
            return Response({
                'error': 'emp does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        empname = self.get_emp_pk(pk)
        serializer1 = EmpSerializer(empname)
        return Response(serializer1.data)

    def put(self, request, pk):
        empname = self.get_emp_pk(pk)
        serializer1 = EmpSerializer(empname, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        empname = self.get_emp_pk(pk)
        empname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Cricket Model  ******************************
class cricketmodels2API(APIView):
    def get(self, request):
        cricketobj = cricketmodel.objects.all()
        cricketserializerobj = cricketSerializer(cricketobj, many=True)
        rerult = cricketserializerobj.data
        return Response(rerult)

class cricketCreate(APIView):
    def post(self, request):
        serializer2 = cricketSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response({'msg':'Data Created...'}, status=status.HTTP_201_CREATED)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)    

class cricketDetail(APIView):

    def get_cricket_pk(self, pk):
        try:
            return cricketmodel.objects.get(id=pk)
        except:
            return Response({
                'error': 'cricket does not exist..'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        cname = self.get_cricket_pk(pk)
        serializer2 = cricketSerializer(cname)
        return Response(serializer2.data)

    def put(self, request, pk):
        cname = self.get_cricket_pk(pk)
        serializer2 = cricketSerializer(cname, data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cname = self.get_cricket_pk(pk)
        cname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)