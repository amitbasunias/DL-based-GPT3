# Generated by Django 4.1.3 on 2022-11-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("writer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useracc",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="useracc",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]