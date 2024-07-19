# Generated by Django 4.2.13 on 2024-07-16 19:55

from django.db import migrations, models
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_report_complain_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='date attended'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(default=myapp.models.current_time, null=True, verbose_name='time in'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(default=myapp.models.current_time, null=True, verbose_name='time out'),
        ),
    ]