# Generated by Django 2.1.5 on 2019-07-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='Contact_no',
            field=models.CharField(max_length=12),
        ),
    ]