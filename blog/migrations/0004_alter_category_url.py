# Generated by Django 5.0.7 on 2024-07-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]