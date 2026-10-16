from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb
from Repository.serializers import QuestionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()  #query the QuestionDb model to retrieve all questions
        serializer_instance=QuestionSerializer(qs,many=True)#serialize the queryset using the Questiiom Serializer
        return Response(data=serializer_instance.data)#Return the serialized data as a response

#adding questions
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
        #creating a new question in the database
            QuestionDb.objects.create(**actual_data)
            return Response(data={"message":"Question added  successfully"})
        else:
            return Response(data={"error":serializer_instance.errors})

#retriving a question by id
class QuestionRetrieveView(APIView):
    def get(self,request,pk):
        qs=QuestionDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response(
            {
                "Message":"Deleted Successfully"
            }
        )

