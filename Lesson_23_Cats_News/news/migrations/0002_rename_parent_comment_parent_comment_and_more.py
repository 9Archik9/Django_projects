# Generated by Django 5.0.1 on 2024-01-31 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent',
            new_name='parent_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
    ]
