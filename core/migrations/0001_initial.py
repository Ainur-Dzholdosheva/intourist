# Generated by Django 3.2.5 on 2021-07-16 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('B', 'Bishkek'), ('C', 'Chui'), ('I', 'Issykkul'), ('N', 'Naryn'), ('T', 'Talas'), ('D', 'Djalalabad'), ('A', 'Batken'), ('O', 'Osh')], max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]