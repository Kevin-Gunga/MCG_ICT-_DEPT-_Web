# Generated by Django 4.2.13 on 2024-07-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_report_email_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='complain_file',
            field=models.FileField(default='complaints/', upload_to='', verbose_name='Complaint File'),
        ),
    ]
