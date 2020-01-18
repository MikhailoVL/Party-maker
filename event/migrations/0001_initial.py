# Generated by Django 3.0.2 on 2020-01-09 16:55

import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('location_ev', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.Place')),
            ],
        ),
    ]