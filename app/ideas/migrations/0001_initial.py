# Generated by Django 3.2.8 on 2021-10-07 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280, verbose_name='content')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('visibility', models.CharField(choices=[('public', 'public'), ('protected', 'protected'), ('private', 'private')], max_length=9, verbose_name='visibility')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
