# Generated by Django 3.2.8 on 2021-11-22 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20211122_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tags',
            new_name='tag',
        ),
    ]
