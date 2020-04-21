# Generated by Django 3.0.5 on 2020-04-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fblink', models.URLField(blank=True, max_length=300, null=True)),
                ('password', models.CharField(max_length=70, null=True)),
                ('activated', models.BooleanField(blank=True, null=True)),
                ('verification_code', models.CharField(blank=True, max_length=70, null=True)),
                ('following', models.ManyToManyField(blank=True, null=True, to='users.User')),
            ],
        ),
    ]