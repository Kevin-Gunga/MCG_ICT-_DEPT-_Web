# Generated by Django 4.2.13 on 2024-07-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_applyattachment_documents_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyattachment',
            name='email',
            field=models.EmailField(blank=True, default='email', max_length=254, null=True),
        ),
    ]
