# Generated by Django 4.0.7 on 2022-08-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0002_alter_changelog_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelog',
            name='object_representation',
            field=models.CharField(blank=True, help_text='Object representation.', max_length=256, null=True, verbose_name='Object representation'),
        ),
    ]
