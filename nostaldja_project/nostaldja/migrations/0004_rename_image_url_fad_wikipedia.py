# Generated by Django 4.2.3 on 2023-07-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0003_alter_fad_decade_alter_fad_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fad',
            old_name='image_url',
            new_name='wikipedia',
        ),
    ]