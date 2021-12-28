from django.db import models


class ITCompany(models.Model):
    id_company = models.AutoField(db_column='ID_company', primary_key=True)
    name_company = models.CharField(db_column='Name_company', max_length=100, blank=True, null=False)
    foundation_year = models.IntegerField(db_column='Foundation_year', blank=True, null=True)
    specialization = models.CharField(db_column='Specialization', max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'IT_Company'
