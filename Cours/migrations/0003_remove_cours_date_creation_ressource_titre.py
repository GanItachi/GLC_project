# Generated by Django 5.0.3 on 2024-10-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0002_remove_ressource_date_creation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='ressource',
            name='titre',
            field=models.CharField(default=5, max_length=200),
            preserve_default=False,
        ),
    ]