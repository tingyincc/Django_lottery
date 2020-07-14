# Generated by Django 2.1.2 on 2019-01-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0011_award_award_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='person',
            name='employee_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]