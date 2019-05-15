from rest_framework import generics

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorList(generics.ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ContributorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
