# Generated by Django 4.0.3 on 2022-07-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='longUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
