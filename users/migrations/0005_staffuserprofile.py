# Generated by Django 5.1.1 on 2024-11-20 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_role_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, choices=[('chat_assistant', 'chat_assistant'), ('manager', 'manager'), ('supervisor', 'supervisor'), ('regular', 'regular')], max_length=255, null=True)),
                ('is_free', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'staff_user_profile',
                'ordering': ['-created_at'],
            },
        ),
    ]
