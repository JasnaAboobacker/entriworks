# Generated by Django 5.0.4 on 2024-05-23 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hospital", "0002_rename_appoinment_appointment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment",
            old_name="date1",
            new_name="appointment_date",
        ),
        migrations.RenameField(
            model_name="appointment",
            old_name="time1",
            new_name="appointment_time",
        ),
    ]
