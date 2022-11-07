# Generated by Django 3.2.7 on 2022-11-06 22:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_main', '0006_alter_connect_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='connected',
            field=models.ManyToManyField(related_name='connected_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]