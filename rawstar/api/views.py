from django import views
from django.http import HttpResponse
from django.views.generic import View

from rest_framework import viewsets
from rest_framework import generics
from .models import AmountReceived, Contestent
from .serializers import AmountReceivedSerializer, ContestentSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view




class ContestentGetCreate(generics.ListCreateAPIView):
  queryset = Contestent.objects.all()
  serializer_class = ContestentSerializer

class ContestentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contestent.objects.all()
  serializer_class = ContestentSerializer

class ImageView(View):
    def get(self, request, image_name):
        try:
            with open(f'singers/{image_name}', 'rb') as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except FileNotFoundError:
            return HttpResponse("Image not found")


class AmountReceivedViewSet(viewsets.ModelViewSet):
    queryset = AmountReceived.objects.all()
    serializer_class = AmountReceivedSerializer

    def create(self, request):
        print(request.data)
        serializer = AmountReceivedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

from django.shortcuts import render
from .models import Contestent

def records_view(request):
    contestents = Contestent.objects.all()
    return render(request, 'index.html', {'contestents': contestents})

#for total vote
from django import template

register = template.Library()

@register.filter
def sum_of_amounts(amount_received_queryset):
    return sum(amount_received.amount for amount_received in amount_received_queryset)


