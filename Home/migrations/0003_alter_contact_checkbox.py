# Generated by Django 4.1.1 on 2023-01-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='checkbox',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
