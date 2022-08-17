# Generated by Django 4.0.7 on 2022-08-17 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credential',
            options={'ordering': ['name'], 'verbose_name': 'Credential', 'verbose_name_plural': 'Credentials'},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['name'], 'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterModelOptions(
            name='devicetype',
            options={'ordering': ['name'], 'verbose_name': 'Device type', 'verbose_name_plural': 'Device types'},
        ),
        migrations.AlterModelOptions(
            name='devicetypetemplate',
            options={'ordering': ['pk'], 'verbose_name': 'Device type template', 'verbose_name_plural': 'Device type templates'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name'], 'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
    ]
