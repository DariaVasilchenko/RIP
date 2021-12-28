from rest_framework import viewsets
from IT_company.serializers import ITCompanySerializer
from IT_company.models import ITCompany


class ITCompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать информацию об IT-компаниях
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = ITCompany.objects.all().order_by('name_company')
    serializer_class = ITCompanySerializer  # Сериализатор для модели