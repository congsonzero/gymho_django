# Generated by Django 2.1.15 on 2021-04-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymho', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
