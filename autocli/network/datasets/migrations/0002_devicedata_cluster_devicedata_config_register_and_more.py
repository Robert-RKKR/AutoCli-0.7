# Generated by Django 4.1 on 2022-10-05 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0002_alter_collecteddata_options_alter_snapshot_options_and_more'),
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedata',
            name='CLUSTER',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='CONFIG_REGISTER',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='DAY',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='DAYWEEK',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='FAILOVER',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='HARDWARE',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='HARDWARE_LIST',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='HOSTNAME',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='IMAGE',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='LICENSE_MODE',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='LICENSE_STATE',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='MAC_LIST',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='MAX_INTF',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='MAX_VLANS',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='MONTH',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='RELOAD_REASON',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='SERIAL',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='SERIAL_LIST',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='TIME',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='TIMEZONE',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME_DAYS',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME_HOURS',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME_MINUTES',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME_WEEKS',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='UPTIME_YEARS',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='VERSION',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='YEAR',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='update',
            field=models.ForeignKey(default=1, help_text='Correlated update model.', on_delete=django.db.models.deletion.CASCADE, to='updates.update', verbose_name='Update model'),
            preserve_default=False,
        ),
    ]
