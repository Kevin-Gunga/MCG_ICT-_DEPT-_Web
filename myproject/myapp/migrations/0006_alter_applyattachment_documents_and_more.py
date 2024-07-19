# Generated by Django 4.2.13 on 2024-07-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_report_department_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyattachment',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='second_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applyattachment',
            name='surname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='complain_file',
            field=models.FileField(blank=True, null=True, upload_to='complaints/'),
        ),
    ]
