# Generated by Django 4.1 on 2022-10-04 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collecteddata',
            options={'ordering': ['-id'], 'verbose_name': 'Collected data', 'verbose_name_plural': 'Collected data'},
        ),
        migrations.AlterModelOptions(
            name='snapshot',
            options={'ordering': ['-id'], 'verbose_name': 'Snapshot', 'verbose_name_plural': 'Snapshots'},
        ),
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ['-id'], 'verbose_name': 'Update', 'verbose_name_plural': 'Update'},
        ),
    ]
