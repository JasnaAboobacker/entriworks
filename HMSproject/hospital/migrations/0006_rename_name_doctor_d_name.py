# Generated by Django 5.0.4 on 2024-06-23 19:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0005_doctor_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctor",
            old_name="name",
            new_name="d_name",
        ),
    ]
