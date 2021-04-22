# Generated by Django 2.1.15 on 2021-04-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymho', '0006_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('LoginID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Login',
                'managed': False,
            },
        ),
    ]