# Generated by Django 2.1.2 on 2019-01-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0012_auto_20190102_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='employee_id',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]