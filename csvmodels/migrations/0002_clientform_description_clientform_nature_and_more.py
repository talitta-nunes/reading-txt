# Generated by Django 4.1.2 on 2023-12-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csvmodels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientform",
            name="description",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="clientform",
            name="nature",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="clientform",
            name="signal",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
