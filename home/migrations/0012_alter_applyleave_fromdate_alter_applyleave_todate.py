# Generated by Django 5.0.1 on 2024-02-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_user_applied_leave"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applyleave",
            name="fromDate",
            field=models.CharField(default="", max_length=250),
        ),
        migrations.AlterField(
            model_name="applyleave",
            name="toDate",
            field=models.CharField(default="", max_length=250),
        ),
    ]
