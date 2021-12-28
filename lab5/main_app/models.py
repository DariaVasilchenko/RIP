from django.db import models


class ITCompany(models.Model):
    id_company = models.AutoField(db_column='ID_company', primary_key=True)
    name_company = models.CharField(db_column='Name_company', max_length=100, blank=True, null=False)
    foundation_year = models.IntegerField(db_column='Foundation_year', blank=True, null=True)
    specialization = models.CharField(db_column='Specialization', max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'IT_Company'


class Founder(models.Model):
    id_founder = models.AutoField(db_column='ID_founder', primary_key=True)
    founder_name = models.CharField(db_column='Founder_name', max_length=100, blank=True, null=False)
    career = models.CharField(db_column='Career', max_length=1000, blank=True, null=True)
    id_company = models.ForeignKey('ITCompany', models.DO_NOTHING, db_column='ID_company', blank=True, null=True)

    class Meta:
        db_table = 'Founder'
