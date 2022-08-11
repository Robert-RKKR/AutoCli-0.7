# Generated by Django 4.1 on 2022-08-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(help_text='Object name.', max_length=128, verbose_name='Name')),
                ('model_name', models.CharField(help_text='Object name.', max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Content type',
                'verbose_name_plural': 'Content types',
                'unique_together': {('app_name', 'model_name')},
            },
        ),
    ]
