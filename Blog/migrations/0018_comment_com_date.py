# Generated by Django 2.1.5 on 2019-08-13 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0017_auto_20190813_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='com_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]