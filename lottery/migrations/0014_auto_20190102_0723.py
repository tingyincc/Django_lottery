# Generated by Django 2.1.2 on 2019-01-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0013_auto_20190102_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='seniority',
            field=models.IntegerField(default=1),
        ),
    ]
