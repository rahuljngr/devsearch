# Generated by Django 3.2.8 on 2021-11-23 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_user'),
        ('projects', '0008_rename_tags_project_tag'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
