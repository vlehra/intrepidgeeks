# Generated by Django 2.1.7 on 2020-01-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_auto_20190908_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]