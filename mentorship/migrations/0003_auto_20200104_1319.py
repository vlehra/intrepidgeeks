# Generated by Django 2.1.7 on 2020-01-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0002_auto_20200104_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='Course2',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Course3',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Course4',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Course5',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Speciality',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
