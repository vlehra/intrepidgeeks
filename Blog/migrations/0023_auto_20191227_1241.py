# Generated by Django 2.1.5 on 2019-12-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0022_delete_ashish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Counselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='acadmics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='mfitness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='opportunites',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='self_dev',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='tech_skills',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='time_manag',
            field=models.BooleanField(default=False),
        ),
    ]
