# Generated by Django 4.1 on 2022-08-07 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contenttype',
            unique_together={('app_name', 'model_name')},
        ),
    ]