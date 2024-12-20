# Generated by Django 5.1.3 on 2024-11-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_id', models.TextField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('web_browser', models.TextField(default=None, null=True)),
                ('user_name', models.TextField(default=None, null=True)),
                ('password', models.TextField(default=None, null=True)),
                ('password_strength', models.TextField(default=None, null=True)),
                ('user_name_field', models.TextField(default=None, null=True)),
                ('password_field', models.TextField(default=None, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_time', models.DateTimeField(auto_now=True, null=True)),
                ('filename', models.TextField(default=None, null=True)),
            ],
        ),
    ]
