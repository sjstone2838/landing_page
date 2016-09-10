from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Registrant
from .serializers import (RegistrantSerializer,)


class RegistrantListCreateView(ListCreateAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer

class RegistrantUpdateView(RetrieveUpdateAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
