# Generated by Django 4.0.6 on 2022-07-30 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
