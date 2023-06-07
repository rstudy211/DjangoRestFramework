# Generated by Django 4.2.2 on 2023-06-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('sal', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
