# Generated by Django 2.1.5 on 2019-08-10 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_remove_blog_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Fifth_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Fourth_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Image_1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Image_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Image_3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Second_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Sixth_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Third_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='first_para',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='writer',
        ),
    ]
