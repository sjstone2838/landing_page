from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Registrant
from .serializers import (RegistrantSerializer,)

from rest_framework import filters


class RegistrantListCreateView(ListCreateAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=email',)

class RegistrantUpdateView(RetrieveUpdateAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
