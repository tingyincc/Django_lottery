# Generated by Django 2.1.2 on 2018-12-01 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='creatre_date',
        ),
    ]
