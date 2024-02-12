# Generated by Django 5.0.1 on 2024-02-12 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_remove_user_applied_leave"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applyleave",
            name="user",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="home.user"
            ),
        ),
    ]
