# Generated by Django 2.1.15 on 2021-04-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('ExerciseID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('rep_recommend', models.CharField(max_length=10)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
    ]
