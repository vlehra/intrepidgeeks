# Generated by Django 2.1.5 on 2019-08-09 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20190808_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Fifth_para',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Fourth_para',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Header_pic',
            field=models.ImageField(default=1, upload_to='static/upload_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Image_1',
            field=models.ImageField(default=1, upload_to='static/upload_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Image_2',
            field=models.ImageField(default=1, upload_to='static/upload_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Image_3',
            field=models.ImageField(default=1, upload_to='static/upload_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Sixth_para',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='Third_para',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
