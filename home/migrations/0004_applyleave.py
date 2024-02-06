# Generated by Django 5.0.1 on 2024-02-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveDesc', models.CharField(default='', max_length=250)),
                ('fromDate', models.DateTimeField()),
                ('toDate', models.DateTimeField()),
                ('selectManager', models.CharField(default='', max_length=30)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
