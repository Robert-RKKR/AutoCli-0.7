# Generated by Django 4.0.7 on 2022-08-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_credential_options_alter_device_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='username',
            field=models.CharField(help_text='Local / remote user name.', max_length=64, verbose_name='Username'),
        ),
    ]
