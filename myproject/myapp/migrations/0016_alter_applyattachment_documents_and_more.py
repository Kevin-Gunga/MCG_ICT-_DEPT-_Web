# Generated by Django 4.2.13 on 2024-07-19 03:33

from django.db import migrations, models
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_applyattachment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyattachment',
            name='documents',
            field=models.FileField(blank=True, default='documents', null=True, upload_to='', verbose_name='documents'),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='first_name',
            field=models.CharField(blank=True, default='first_name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='id_number',
            field=models.CharField(blank=True, default='id_number', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='institution_name',
            field=models.CharField(blank=True, default='institution_name', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='phone_number',
            field=models.CharField(blank=True, default='phone_number', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='second_name',
            field=models.CharField(blank=True, default='second_name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='surname',
            field=models.CharField(blank=True, default='surname', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='date attended'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='full_name',
            field=models.CharField(blank=True, default='full_name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='id_num',
            field=models.CharField(blank=True, default='id_num', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(blank=True, default=myapp.models.current_time, null=True, verbose_name='time in'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(blank=True, default=myapp.models.current_time, null=True, verbose_name='time out'),
        ),
        migrations.AlterField(
            model_name='report',
            name='complain_text',
            field=models.TextField(default='complaints', null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='department_text',
            field=models.CharField(blank=True, default='department', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='email_text',
            field=models.EmailField(blank=True, default='email', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='phone_number',
            field=models.CharField(blank=True, default='phone', max_length=15, null=True),
        ),
    ]
