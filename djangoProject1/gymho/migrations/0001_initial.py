# Generated by Django 3.1.7 on 2021-04-03 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Execise',
            fields=[
                ('ExeciseID', models.IntegerField(max_length='10', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('rep_recommend', models.CharField(max_length=10)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
    ]
