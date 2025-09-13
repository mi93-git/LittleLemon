from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# alternative: from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# create list  (GET / POST)
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# read/change/delete single object (GET / PUT/PATCH / DELETE)
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]