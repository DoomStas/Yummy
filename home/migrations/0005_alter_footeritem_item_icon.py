# Generated by Django 5.1.1 on 2024-10-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_footeritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footeritem',
            name='item_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
