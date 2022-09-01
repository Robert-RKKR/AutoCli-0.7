# Generated by Django 4.1 on 2022-08-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_setting_description_setting_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='current',
            field=models.BooleanField(default=False, help_text='Current main application settings.', verbose_name='Current'),
        ),
    ]