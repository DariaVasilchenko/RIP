from IT_company.models import ITCompany
from rest_framework import serializers


class ITCompanySerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = ITCompany
        # Поля, которые мы сериализуем
        fields = ["id_company", "name_company", "foundation_year", "specialization"]