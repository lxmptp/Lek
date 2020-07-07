# Generated by Django 3.0.7 on 2020-06-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listForRegistration', '0007_auto_20200627_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredusers',
            name='mail',
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='date_joined',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='is_active',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='is_staff',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]