from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from adminstration.permissions import ReadOnly
from adminstration.serializers import SecaoSerializer, GraduacaoSerializer, MilitarSerializer
from adminstration.models import Secao, Graduacao, Militar

class SecaoViewSet(viewsets.ModelViewSet):
    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class GraduacaoViewSet(viewsets.ModelViewSet):
    queryset = Graduacao.objects.all()
    serializer_class = GraduacaoSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class MilitarViewSet(viewsets.ModelViewSet):
    queryset = Militar.objects.all()
    serializer_class = MilitarSerializer
    permission_classes = [IsAdminUser|ReadOnly]