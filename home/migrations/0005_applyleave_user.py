# Generated by Django 5.0.1 on 2024-02-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_applyleave'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyleave',
            name='user',
            field=models.CharField(default='', max_length=30),
        ),
    ]
