# Generated by Django 4.1.5 on 2023-01-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advertise_category_alter_advertise_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
