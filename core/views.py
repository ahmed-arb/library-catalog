from core.models import Author, Book, Loan
from core.serializers import AuthorSerializer, BookSerializer, LoanSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
