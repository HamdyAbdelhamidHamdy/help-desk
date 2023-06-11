# Generated by Django 4.2.1 on 2023-06-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0003_remove_ticket_status_ticket_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Open"),
                    ("2", "Reopened"),
                    ("3", "Resolved"),
                    ("4", "Closed"),
                    ("5", "Duplicate"),
                ],
                default="1",
                max_length=1,
            ),
        ),
    ]
