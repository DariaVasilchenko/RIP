from django.db import models


class Processor(models.Model):
    """Микропроцессор"""
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=150, blank=True)
    memory_cash = models.IntegerField(db_column='Memory cash', blank=True, null=True)
    frequency = models.IntegerField(db_column='Frequency', blank=True, null=True)

    class Meta:
        db_table = 'Processor'

    def __str__(self):
        return f'{self.name}'


class PC(models.Model):
    """Компьютер"""
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, blank=True)
    price = models.IntegerField(db_column='Price', blank=True, null=True)
    processor_id = models.ForeignKey('Processor', models.DO_NOTHING, db_column='Processor_id')

    class Meta:
        db_table = 'PC'

    def __str__(self):
        return f'{self.name}'
