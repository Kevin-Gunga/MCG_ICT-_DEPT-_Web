# Generated by Django 4.2.13 on 2024-07-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_report_complain_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='email_text',
            field=models.EmailField(blank=True, default='email', max_length=254, null=True),
        ),
    ]
