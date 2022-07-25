from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from .models import Book


# Create your views here.

# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.filter(show_site=True)
#         return render(request, 'account/book_list.html', {'books': books})

class Home(APIView):
    def get(self, request):
        return Response({'name': 'ali'})
