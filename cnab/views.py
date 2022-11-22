from rest_framework import generics
from .models import Cnab
from .serializers import CnabSerializer


class CnabView(generics.ListCreateAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer
