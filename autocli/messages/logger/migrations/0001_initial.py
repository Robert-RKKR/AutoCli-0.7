# Generated by Django 4.0.7 on 2022-08-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Time of the log creation.', verbose_name='Timestamp')),
                ('app_name', models.CharField(help_text='Name of the object application.', max_length=64, verbose_name='Object application name')),
                ('model_name', models.CharField(help_text='Name of the object model.', max_length=64, verbose_name='Object model name')),
                ('object_id', models.IntegerField(blank=True, help_text='Correlated object ID representation.', null=True, verbose_name='Object ID')),
                ('application', models.CharField(help_text='Name of the application which triggered the log.', max_length=64, verbose_name='Application')),
                ('code_id', models.CharField(blank=True, help_text='ID indicating the location of the log call in the code.', max_length=64, null=True, verbose_name='Code ID')),
                ('task_id', models.CharField(blank=True, help_text='ID of the task associated with the log.', max_length=64, null=True, verbose_name='Task ID')),
                ('severity', models.IntegerField(choices=[(1, 'CRITICAL'), (2, 'ERROR'), (3, 'WARNING'), (4, 'INFO'), (5, 'DEBUG')], help_text='Log severity.', verbose_name='Severity')),
                ('message', models.CharField(help_text='Log message.', max_length=128, verbose_name='Message')),
                ('execution', models.FloatField(blank=True, help_text='Log task completion time.', null=True, verbose_name='Execution time')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'ordering': ['-pk'],
            },
        ),
    ]
