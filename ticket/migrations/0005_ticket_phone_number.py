# Generated by Django 4.2.1 on 2023-06-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0004_ticket_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="phone_number",
            field=models.CharField(default=0, max_length=20),
        ),
    ]