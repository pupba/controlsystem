# Generated by Django 4.1 on 2023-04-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleprocessing', '0003_rename_password_operator_op_pw'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipInfo',
            fields=[
                ('shipname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sog', models.IntegerField()),
                ('cog', models.FloatField(max_length=100)),
                ('connect', models.BooleanField(max_length=100)),
                ('stage', models.IntegerField()),
                ('gps', models.CharField(max_length=100)),
                ('ais', models.BooleanField(max_length=100)),
                ('ssas', models.BooleanField(max_length=100)),
                ('speaker', models.BooleanField(max_length=100)),
                ('eb', models.BooleanField(max_length=100)),
            ],
        ),
    ]