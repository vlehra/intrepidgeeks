# Generated by Django 2.1.5 on 2019-07-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=35)),
                ('Email', models.CharField(max_length=35)),
                ('Contact_no', models.CharField(max_length=12, unique=True)),
                ('Message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
