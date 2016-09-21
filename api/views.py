from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Registrant
from .serializers import (RegistrantSerializer,)


class RegistrantCreateUpdateView(CreateAPIView):

    serializer_class = RegistrantSerializer

    def post(self, request, * args, **kwargs):
        data = request.data
        data = dict((k, v) for k, v in data.iteritems() if v)

        registrant, created = Registrant.objects.update_or_create(
            email=data['email'],
            defaults=data
        )

        return Response({"detail": "Your request has been submitted."})
