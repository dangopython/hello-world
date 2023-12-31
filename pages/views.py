"""
    Pages View
"""
from django.http import HttpResponse


def home_page_view(request) -> HttpResponse:
    return HttpResponse("Hello, World!")
