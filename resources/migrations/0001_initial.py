# Generated by Django 4.1.3 on 2022-11-16 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesCategory',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=100)),
                ('CategoryOccupation', models.CharField(max_length=100)),
                ('CategoryDescription', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/resources/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('practice_names', models.CharField(default='', max_length=100)),
                ('education', models.TextField(default='')),
                ('mobile_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('zip_code', models.IntegerField()),
                ('address', models.CharField(default='', max_length=100)),
                ('introduction', models.TextField()),
                ('speciality', models.CharField(default='', max_length=100)),
                ('linkdin_profile', models.CharField(default='', max_length=100)),
                ('rating', models.IntegerField()),
                ('link', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='media/profile/')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.resourcescategory')),
            ],
        ),
    ]