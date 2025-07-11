# Generated by Django 5.2.3 on 2025-07-03 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_lessons_video_lessons_video'),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('resource', 'Resource Added'), ('video', 'Video Uploaded'), ('note', 'Note Added'), ('new_course', 'New Course'), ('upcoming_course', 'Upcoming Course')], max_length=20)),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
        ),
    ]
