# Generated by Django 4.1 on 2022-09-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='application',
            field=models.CharField(default='rtr', help_text='Name of the application which triggered the notification.', max_length=64, verbose_name='Application'),
            preserve_default=False,
        ),
    ]
