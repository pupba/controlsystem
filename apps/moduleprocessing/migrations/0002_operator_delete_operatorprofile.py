# Generated by Django 4.1 on 2023-03-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduleprocessing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='OperatorProfile',
        ),
    ]