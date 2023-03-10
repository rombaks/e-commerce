# Generated by Django 4.1.6 on 2023-02-09 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("rating", models.IntegerField(blank=True, default=0, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
