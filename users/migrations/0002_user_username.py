# Generated by Django 5.0.2 on 2024-02-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
