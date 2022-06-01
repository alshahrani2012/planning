# Generated by Django 4.0.2 on 2022-04-12 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Schools', '0007_school_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_nu', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200, null=True)),
                ('subject', models.TextField(null=True)),
                ('private', models.BooleanField(default=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_create', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]