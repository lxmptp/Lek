# Generated by Django 3.0.7 on 2020-07-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listForRegistration', '0012_auto_20200703_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredusers',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]