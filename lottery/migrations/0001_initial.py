# Generated by Django 2.1.2 on 2018-12-01 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.IntegerField(default=9999, primary_key=True, serialize=False)),
                ('first_selection', models.IntegerField(default=10)),
                ('second_selection', models.IntegerField(default=1)),
                ('exclude_seniority', models.CharField(max_length=20)),
                ('is_done', models.BooleanField(default=False)),
                ('award_name', models.CharField(max_length=20)),
                ('descript_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('seniority', models.CharField(max_length=10)),
                ('is_attend', models.BooleanField(default=True)),
                ('creatre_date', models.DateTimeField(verbose_name='date created')),
                ('award', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lottery.Award')),
            ],
        ),
    ]
