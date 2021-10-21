# Generated by Django 3.2.8 on 2021-10-21 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0004_alter_bookmark_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='files',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='files',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to='paper.files'),
            preserve_default=False,
        ),
    ]