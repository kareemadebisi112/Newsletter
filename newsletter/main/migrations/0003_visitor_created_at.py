# Generated by Django 5.0.1 on 2024-02-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_visitor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
