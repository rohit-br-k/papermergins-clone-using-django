# Generated by Django 3.2.8 on 2021-10-21 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_bookmark_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.files'),
        ),
    ]