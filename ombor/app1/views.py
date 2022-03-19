from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer
    permission_classes = [IsAuthenticated,]


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSer
    permission_classes = [IsAuthenticated, ]


class StatsViewSet(ModelViewSet):
    queryset = Stats.objects.all()
    serializer_class = StatsSer
    permission_classes = [IsAuthenticated, ]


class OmborViewSet(ModelViewSet):
    queryset = Ombor.objects.all()
    serializer_class = OmborSer
    permission_classes = [IsAuthenticated, ]
