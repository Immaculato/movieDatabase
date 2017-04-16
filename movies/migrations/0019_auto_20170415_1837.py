# Generated by Django 2.0.dev20170322162159 on 2017-04-15 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_merge_20170415_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='review',
        ),
        migrations.RemoveField(
            model_name='user',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.User'),
        ),
    ]
