# Generated by Django 2.2.5 on 2020-01-08 22:30

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=100, unique=True)),
                ('DestinationLocation', models.CharField(max_length=30)),
                ('SourceLocation', models.CharField(max_length=30)),
                ('Image', models.CharField(max_length=200)),
                ('TripStartDate', models.DateField()),
                ('TripEndDate', models.DateField()),
                ('Accommodation', models.CharField(max_length=30)),
                ('TripCost', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            managers=[
                ('TravelLists', django.db.models.manager.Manager()),
            ],
        ),
    ]