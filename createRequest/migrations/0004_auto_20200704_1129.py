# Generated by Django 3.0.7 on 2020-07-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createRequest', '0003_auto_20200702_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='docrequestlist',
            name='date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='docrequestlist',
            name='version',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]