from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from .filters import TourFilter
from .models import Booking, Category, Review, Tour
from .pagination import CustomPagination
from .serializers import (
    BookingSerializer,
    CategorySerializer,
    ReviewSerializer,
    TourDetailSerializer,
    TourListSerializer,
)


class TourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = TourFilter
    serializer_class = TourListSerializer


class TourDetailAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class RecommendTourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.exclude(season__isnull=True).order_by("season")
    serializer_class = TourListSerializer

