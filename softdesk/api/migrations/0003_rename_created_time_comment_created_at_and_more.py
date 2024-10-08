# Generated by Django 4.2.9 on 2024-08-23 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='created_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='created_time',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
