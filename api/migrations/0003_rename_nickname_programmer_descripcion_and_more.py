# Generated by Django 5.1.2 on 2024-10-16 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_programmer_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='nickname',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='programmer',
            old_name='fullname',
            new_name='nombre',
        ),
    ]
