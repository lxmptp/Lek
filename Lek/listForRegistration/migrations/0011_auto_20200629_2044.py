# Generated by Django 3.0.7 on 2020-06-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listForRegistration', '0010_auto_20200629_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Наименование роли '),
        ),
    ]
