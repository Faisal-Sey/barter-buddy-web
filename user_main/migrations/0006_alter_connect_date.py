# Generated by Django 3.2.7 on 2022-11-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_main', '0005_connect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
