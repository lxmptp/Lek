# Generated by Django 3.0.7 on 2020-06-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listForRegistration', '0003_auto_20200627_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredusers',
            name='usernames',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
