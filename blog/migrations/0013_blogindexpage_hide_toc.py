# Generated by Django 3.2.14 on 2022-08-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blogpage_body_mixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='hide_toc',
            field=models.BooleanField(default=False, verbose_name='Hide Table of Contents'),
        ),
    ]