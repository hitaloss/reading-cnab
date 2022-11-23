from .serializers import CnabSerializer
from rest_framework import generics
from .models import Cnab


class CnabView(generics.ListCreateAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer
