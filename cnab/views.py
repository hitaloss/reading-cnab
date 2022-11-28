from django.shortcuts import render
from .serializers import CnabSerializer
from rest_framework import viewsets
from .models import Cnab


class CnabView(viewsets.ModelViewSet):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer

    # def model_form_upload(request):
    #     if request.method == "POST":
    #         form = CnabForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
