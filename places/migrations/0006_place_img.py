# Generated by Django 3.2.5 on 2021-07-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_feedback_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='places'),
        ),
    ]
