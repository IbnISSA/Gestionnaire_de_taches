# Generated by Django 4.2.5 on 2023-09-09 03:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="Created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="Finished_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]
