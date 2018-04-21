from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from datatable.humans.models import Human
from datatable.humans.serializers import HumanSerializer


class HumanList(ListCreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer


class HumanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
