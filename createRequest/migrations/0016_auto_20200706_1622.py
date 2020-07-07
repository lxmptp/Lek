# Generated by Django 3.0.7 on 2020-07-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createRequest', '0015_auto_20200706_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrequestlist',
            name='date_test',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='date_zagolovok',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='num_test',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='num_zagolovok',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='test',
            field=models.FileField(blank=True, max_length=30, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='docrequestlist',
            name='zagolovok',
            field=models.FileField(upload_to='zagolovok/'),
        ),
    ]