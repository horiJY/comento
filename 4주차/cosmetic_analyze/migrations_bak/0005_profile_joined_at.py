# Generated by Django 3.1.7 on 2021-03-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_analyze', '0004_remove_profile_joined_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-03-14'),
            preserve_default=False,
        ),
    ]
