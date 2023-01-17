from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import Author, Book, Loan, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "borrower", "date_borrowed", "date_due", "date_returned")


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email"),
            },
        ),
    )
