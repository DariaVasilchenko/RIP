# Generated by Django 4.0 on 2021-12-19 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=150)),
                ('memory_cash', models.IntegerField(blank=True, db_column='Memory cash', null=True)),
                ('frequency', models.IntegerField(blank=True, db_column='Frequency', null=True)),
            ],
            options={
                'db_table': 'Processor',
            },
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100)),
                ('price', models.IntegerField(blank=True, db_column='Price', null=True)),
                ('processor_id', models.ForeignKey(db_column='Processor_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.processor')),
            ],
            options={
                'db_table': 'PC',
            },
        ),
    ]
