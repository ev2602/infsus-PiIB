# Generated by Django 5.0.6 on 2024-05-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAdmin', models.CharField(default='', max_length=8, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
