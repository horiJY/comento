# Generated by Django 3.1.7 on 2021-03-10 05:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cosmetic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('maker', models.CharField(max_length=30)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('rank', models.PositiveSmallIntegerField()),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('award', models.CharField(max_length=200, null=True)),
                ('launch_at', models.DateField()),
                ('category_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Cosmetic_category', to='cosmetic_analyze.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=128, verbose_name='사용자이메일')),
                ('skin_type', models.PositiveIntegerField(verbose_name='피부타입 (지성,건성,민감성 맞으면 1 아니면 0)')),
                ('joined_at', models.ForeignKey(db_column='date_joined', on_delete=django.db.models.deletion.CASCADE, related_name='Profile_joindate', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oily_skin', models.CharField(max_length=30)),
                ('dry_skin', models.CharField(max_length=30)),
                ('sensitivet_skin', models.CharField(max_length=30)),
                ('Whitening', models.BooleanField(default=False)),
                ('UV', models.BooleanField(default=False)),
                ('Wrinkle', models.BooleanField(default=False)),
                ('purified_water', models.BooleanField(default=False)),
                ('colorant', models.BooleanField(default=False)),
                ('paraben', models.BooleanField(default=False)),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Ingredient_productid', to='cosmetic_analyze.cosmetic')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strengths', models.TextField()),
                ('weaknesses', models.TextField()),
                ('image_url', models.SlugField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_auth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
