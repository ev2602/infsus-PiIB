# Generated by Django 5.0.6 on 2024-05-26 12:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_category_delete_admin_bicycle_rentbicycle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentbicycle',
            name='reservedDates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), default=list, size=None),
        ),
    ]
