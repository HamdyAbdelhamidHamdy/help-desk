# Generated by Django 4.2.1 on 2023-06-06 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
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
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("critical", "Critical"),
                            ("high", "High"),
                            ("normal", "Normal"),
                            ("low", "Low"),
                            ("verylow", "Very Low"),
                        ],
                        default="low",
                        max_length=20,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="category.category",
                    ),
                ),
            ],
        ),
    ]
