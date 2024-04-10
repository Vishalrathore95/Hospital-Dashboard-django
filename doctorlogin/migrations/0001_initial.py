# Generated by Django 5.0.3 on 2024-03-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('years_of_experience', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
            ],
        ),
    ]
