# Generated by Django 4.0 on 2021-12-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itcompany',
            name='name_company',
            field=models.CharField(blank=True, db_column='Name_company', max_length=100),
        ),
    ]
