# Generated by Django 3.1.7 on 2021-03-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_analyze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Comment_productid', to='cosmetic_analyze.cosmetic'),
            preserve_default=False,
        ),
    ]
