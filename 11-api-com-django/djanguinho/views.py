from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# Views

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

# APIs

@api_view(['GET'])
def api_status(request: Request) -> Response:
    return Response({
        "status": "ok",
        "authenticated": request.user.is_authenticated,
        "username": request.user.username,
    }, status=status.HTTP_200_OK)
