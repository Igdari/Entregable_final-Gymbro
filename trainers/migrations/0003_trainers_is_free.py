# Generated by Django 4.1.6 on 2023-02-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_remove_trainers_is_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainers',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]