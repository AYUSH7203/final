# Generated by Django 5.0.3 on 2024-04-18 20:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="pimage",
        ),
    ]
