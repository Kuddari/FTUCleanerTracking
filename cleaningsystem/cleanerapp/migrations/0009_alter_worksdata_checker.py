# Generated by Django 4.2.5 on 2023-09-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cleanerapp", "0008_alter_worksdata_checker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worksdata",
            name="checker",
            field=models.CharField(max_length=100),
        ),
    ]
