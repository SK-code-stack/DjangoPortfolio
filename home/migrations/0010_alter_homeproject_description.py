# Generated by Django 5.2 on 2025-07-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homeproject_image_alter_intro_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeproject',
            name='description',
            field=models.CharField(),
        ),
    ]
