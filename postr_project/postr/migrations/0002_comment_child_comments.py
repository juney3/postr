# Generated by Django 2.0.5 on 2018-06-09 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='child_comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='postr.Comment'),
        ),
    ]
