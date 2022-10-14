# Generated by Django 4.1 on 2022-10-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetypetemplate',
            name='device_data_corelation',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Access list data'), (2, 'ARP table data'), (3, 'Device data'), (4, 'DMVPN data'), (5, 'Environment data'), (6, 'Etherchannel data'), (7, 'Interface data'), (8, 'MAC table data'), (9, 'Module data'), (10, 'Neighbor data'), (11, 'NHRP data'), (12, 'Router data')], default=0, help_text='Correlated device data model.', verbose_name='Correlated device data model'),
        ),
    ]
