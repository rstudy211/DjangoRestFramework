# Generated by Django 4.2.2 on 2023-06-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
