# Generated by Django 2.1.2 on 2019-01-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0014_auto_20190102_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]