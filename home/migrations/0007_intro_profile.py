# Generated by Django 5.2 on 2025-06-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profilePic/'),
        ),
    ]
