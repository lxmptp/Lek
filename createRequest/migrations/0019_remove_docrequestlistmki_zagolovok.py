# Generated by Django 3.0.7 on 2020-07-15 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createRequest', '0018_auto_20200715_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docrequestlistmki',
            name='zagolovok',
        ),
    ]