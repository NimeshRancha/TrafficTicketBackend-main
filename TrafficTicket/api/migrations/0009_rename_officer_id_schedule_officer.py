# Generated by Django 4.2.5 on 2023-10-13 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='officer_id',
            new_name='officer',
        ),
    ]
