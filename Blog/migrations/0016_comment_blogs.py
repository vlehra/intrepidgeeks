# Generated by Django 2.1.5 on 2019-08-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_auto_20190813_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blogs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.Blog'),
            preserve_default=False,
        ),
    ]
