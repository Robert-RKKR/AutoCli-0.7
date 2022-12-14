# Generated by Django 4.1 on 2022-10-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicedata',
            old_name='CLUSTER',
            new_name='cluster',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='CONFIG_REGISTER',
            new_name='config_register',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='DAY',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='DAYWEEK',
            new_name='dayweek',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='FAILOVER',
            new_name='failover',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='HARDWARE',
            new_name='hardware',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='HARDWARE_LIST',
            new_name='hardware_list',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='HOSTNAME',
            new_name='hostname',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='IMAGE',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='LICENSE_MODE',
            new_name='license_mode',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='LICENSE_STATE',
            new_name='license_state',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='MAC_LIST',
            new_name='mac_list',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='MAX_INTF',
            new_name='max_intf',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='MAX_VLANS',
            new_name='max_vlans',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='MONTH',
            new_name='month',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='RELOAD_REASON',
            new_name='reload_reason',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='SERIAL',
            new_name='serial',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='SERIAL_LIST',
            new_name='serial_list',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='TIME',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='TIMEZONE',
            new_name='timezone',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME',
            new_name='uptime',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME_DAYS',
            new_name='uptime_days',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME_HOURS',
            new_name='uptime_hours',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME_MINUTES',
            new_name='uptime_minutes',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME_WEEKS',
            new_name='uptime_weeks',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='UPTIME_YEARS',
            new_name='uptime_years',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='VERSION',
            new_name='version',
        ),
        migrations.RenameField(
            model_name='devicedata',
            old_name='YEAR',
            new_name='year',
        ),
        migrations.AlterField(
            model_name='devicedata',
            name='update',
            field=models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', unique=True, verbose_name='Update model'),
        ),
        migrations.CreateModel(
            name='RouterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Router data',
                'verbose_name_plural': 'Router data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NhrpData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'NHRP data',
                'verbose_name_plural': 'NHRP data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NeighborData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Neighbor data',
                'verbose_name_plural': 'Neighbor data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ModuleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Module data',
                'verbose_name_plural': 'Module data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MacTableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('vlan', models.CharField(blank=True, max_length=32, null=True)),
                ('mac', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.CharField(blank=True, max_length=32, null=True)),
                ('secure', models.CharField(blank=True, max_length=32, null=True)),
                ('ntfy', models.CharField(blank=True, max_length=32, null=True)),
                ('ports', models.CharField(blank=True, max_length=32, null=True)),
                ('ports_list', models.JSONField(blank=True, null=True)),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'MAC Table data',
                'verbose_name_plural': 'MAC Table data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InterfaceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Interface data',
                'verbose_name_plural': 'Interface data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EtherchannelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Etherchannel data',
                'verbose_name_plural': 'Etherchannel data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EnvironmentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Environment data',
                'verbose_name_plural': 'Environment data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DmvpnData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'DMVPN data',
                'verbose_name_plural': 'DMVPN data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ArpTableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('Protocol', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.CharField(blank=True, max_length=32, null=True)),
                ('mac', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('interface', models.CharField(blank=True, max_length=32, null=True)),
                ('physical_interface', models.CharField(blank=True, max_length=32, null=True)),
                ('cpu', models.CharField(blank=True, max_length=32, null=True)),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'ARP table data',
                'verbose_name_plural': 'ARP table data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AccessListData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, help_text='Is object deleted.', verbose_name='Deleted')),
                ('root', models.BooleanField(default=False, help_text='Root object cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Object status.', verbose_name='Active')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('sn', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('interface', models.CharField(blank=True, max_length=32, null=True)),
                ('interface_direction', models.CharField(blank=True, max_length=32, null=True)),
                ('update', models.ForeignKey(help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model')),
            ],
            options={
                'verbose_name': 'Access list data',
                'verbose_name_plural': 'Access list data',
                'ordering': ['-id'],
                'unique_together': {('update', 'name', 'sn')},
            },
        ),
    ]
