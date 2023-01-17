from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Name of the book.")
    authors = models.ManyToManyField(
        Author,
        help_text="Reference field for Authors. There can be more than one Author.",
    )

    def __str__(self) -> str:
        return self.title


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="Reference field for book.")
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who borrowed this book")
    date_borrowed = models.DateField(
        help_text="Date field for when the book was borrowed. Format: <em>YYYY-MM-DD</em>."
    )
    date_due = models.DateField(help_text="Date Field for when the book is due. Format: <em>YYYY-MM-DD</em>.")
    date_returned = models.DateField(
        null=True,
        blank=True,
        help_text="Nullable date Field for when the book is returned. Format: <em>YYYY-MM-DD</em>.",
    )
