# Generated by Django 4.0.7 on 2022-08-15 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import inventory.all.base_model.all.validators
import inventory.devices.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Object name.', max_length=32, unique=True, validators=[inventory.all.base_model.all.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(blank=True, default='Object default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Object description.', max_length=256, null=True, validators=[inventory.all.base_model.all.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='Object graphical representation.', verbose_name='Object ico')),
                ('color', models.IntegerField(default=1, help_text='Color object mark.', verbose_name='Object color')),
                ('username', models.CharField(error_messages={'blank': 'Username field is mandatory.', 'invalid': 'Enter the correct username value.', 'null': 'Username field is mandatory.'}, help_text='Local / remote user name.', max_length=64, verbose_name='Username')),
                ('password', models.CharField(help_text='Local / remote user password.', max_length=64, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
                'ordering': ['name'],
                'permissions': [('read_only', 'read_write')],
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Object name.', max_length=32, unique=True, validators=[inventory.all.base_model.all.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(blank=True, default='Object default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Object description.', max_length=256, null=True, validators=[inventory.all.base_model.all.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='Object graphical representation.', verbose_name='Object ico')),
                ('color', models.IntegerField(default=1, help_text='Color object mark.', verbose_name='Object color')),
                ('hostname', models.CharField(error_messages={'blank': 'IP / DNS name field is mandatory.', 'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.', 'null': 'IP / DNS name field is mandatory.', 'unique': 'Device with this hostname already exists.'}, help_text='Valid IP address or domain name.', max_length=32, unique=True, validators=[inventory.devices.validators.HostnameValueValidator()], verbose_name='Hostname')),
                ('ssh_port', models.IntegerField(blank=True, help_text='SSH protocol port number.', null=True, verbose_name='SSH port')),
                ('https_port', models.IntegerField(blank=True, help_text='HTTPS protocol port number.', null=True, verbose_name='HTTPS port')),
                ('ssh_status', models.BooleanField(default=False, help_text='Status of SSH connection to the device.', verbose_name='SSH status')),
                ('https_status', models.BooleanField(default=False, help_text='Status of HTTPS connection to the device.', verbose_name='HTTPS status')),
                ('secret', models.CharField(blank=True, help_text='Network device secret password.', max_length=64, null=True, verbose_name='Secret password')),
                ('token', models.CharField(blank=True, help_text='Network device API key.', max_length=128, null=True, verbose_name='API token')),
                ('certificate', models.BooleanField(default=False, help_text='Check network device certificate during HTTPS connection.', verbose_name='Certificate')),
                ('credential', models.ForeignKey(blank=True, help_text='Credential needed to establish SSH / HTTPS connection.', null=True, on_delete=django.db.models.deletion.PROTECT, to='devices.credential', verbose_name='Credential')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['name'],
                'permissions': [('read_only', 'read_write')],
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Object name.', max_length=32, unique=True, validators=[inventory.all.base_model.all.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(blank=True, default='Object default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Object description.', max_length=256, null=True, validators=[inventory.all.base_model.all.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='Object graphical representation.', verbose_name='Object ico')),
                ('color', models.IntegerField(default=1, help_text='Color object mark.', verbose_name='Object color')),
                ('netmiko_name', models.CharField(help_text='Netmiko name.', max_length=32, unique=True, verbose_name='Netmiko name')),
            ],
            options={
                'verbose_name': 'Device type',
                'verbose_name_plural': 'Device types',
                'ordering': ['name'],
                'permissions': [('read_only', 'read_write')],
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Object name.', max_length=32, unique=True, validators=[inventory.all.base_model.all.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(blank=True, default='Object default description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Object description.', max_length=256, null=True, validators=[inventory.all.base_model.all.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.IntegerField(default=1, help_text='Object graphical representation.', verbose_name='Object ico')),
                ('color', models.IntegerField(default=1, help_text='Color object mark.', verbose_name='Object color')),
                ('ssh_port', models.IntegerField(blank=True, help_text='SSH protocol port number.', null=True, verbose_name='Default SSH port')),
                ('https_port', models.IntegerField(blank=True, help_text='HTTPS protocol port number.', null=True, verbose_name='Default HTTPS port')),
                ('secret', models.CharField(blank=True, help_text='Network device secret password.', max_length=64, null=True, verbose_name='Default secret password')),
                ('token', models.CharField(blank=True, help_text='Network device API key.', max_length=128, null=True, verbose_name='Default API token')),
                ('certificate', models.BooleanField(blank=True, help_text='Check network device certificate during HTTPS connection.', null=True, verbose_name='Default certificate')),
                ('credential', models.ForeignKey(blank=True, help_text='Credential needed to establish SSH / HTTPS connection.', null=True, on_delete=django.db.models.deletion.PROTECT, to='devices.credential', verbose_name='Default credential')),
                ('devices', models.ManyToManyField(help_text='All devices that belongs to current folder.', to='devices.device', verbose_name='Devices')),
                ('root_folder', models.ForeignKey(blank=True, help_text='The parent folder to witch the current folder belongs.', null=True, on_delete=django.db.models.deletion.PROTECT, to='devices.group', verbose_name='Root folder')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['name'],
                'permissions': [('read_only', 'read_write')],
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(blank=True, help_text='Type of network device system.', null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.devicetype', verbose_name='Device type'),
        ),
        migrations.CreateModel(
            name='DeviceTypeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('special', models.BooleanField(default=False, help_text='Spacial type of Device type template object.', verbose_name='Special template')),
                ('vrf', models.BooleanField(default=False, help_text='VRF cli command template.', verbose_name='VRF template')),
                ('command', models.CharField(blank=True, help_text='CLI command that will be executed on network device.', max_length=64, null=True, verbose_name='CLI command')),
                ('sfm_expression', models.TextField(blank=True, help_text='SFM expression used to check if CLI command/s output is correct.', null=True, verbose_name='SFM expression')),
                ('device_type', models.ForeignKey(help_text='Type of network device system.', on_delete=django.db.models.deletion.PROTECT, to='devices.devicetype', verbose_name='Device type')),
            ],
            options={
                'verbose_name': 'Device type template',
                'verbose_name_plural': 'Device type templates',
                'ordering': ['pk'],
                'permissions': [('read_only', 'read_write')],
                'unique_together': {('command', 'device_type')},
            },
        ),
    ]
