# Generated by Django 4.0.2 on 2022-03-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0005_alter_school_latitude_alter_school_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='office',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]