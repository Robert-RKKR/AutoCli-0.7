# Generated by Django 4.0.7 on 2022-08-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, help_text='Time of the change creation.', verbose_name='Timestamp'),
        ),
    ]
