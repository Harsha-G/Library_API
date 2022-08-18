from django.shortcuts import render

from datetime import datetime
from urllib.request import Request
from django.shortcuts import render

from endpoint.models import Book
from endpoint.serializers import BookSerializer

from rest_framework.response import Response
from rest_framework import views, viewsets

from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import generics

from rest_framework import status

class List_Books(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Add_Book(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Delete_All_Books(views.APIView):
    def delete(self, request):
        Book.objects.all().delete()
        return (Response(status=status.HTTP_204_NO_CONTENT)) 

class Get_Book_By_Author(views.APIView):
    def post(self, request, format=None):
        auth_ = request.data.get("author")
        if(auth_):
            qs = BookSerializer(Book.objects.filter(author=auth_), many=True)
            return (Response(qs.data))
        else:
            exception_msg = {'message':'The Author you entered does not exist'}
            return Response(exception_msg, status=status.HTTP_404_NOT_FOUND)
           

class Get_Book_By_Genre(views.APIView):
    def post(self, request, format=None):
        genre_ = request.data.get("genre")
        if(genre_):
            qs = BookSerializer(Book.objects.filter(genre=genre_), many=True)
            return (Response(qs.data))
        else:
            exception_msg = {'message':'The Genre you entered does not exist'}
            return Response(exception_msg, status=status.HTTP_404_NOT_FOUND)


class Get_Book_Titles(views.APIView):
    def get(self, request, format=None):
        title_arr = [book_.title for book_ in Book.objects.all()]

        return (Response(title_arr))

class Get_BookCount(views.APIView):
    def get(self, request, format=None):
        count = Book.objects.count()
        now = datetime.now()

        payload = {
            "date_and_time" : str(now),
            "total_book_count" : str(count)
        }

        return (Response(payload))
