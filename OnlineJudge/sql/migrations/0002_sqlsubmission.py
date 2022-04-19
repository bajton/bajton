# Generated by Django 2.1.7 on 2022-04-17 18:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import utils.shortcuts


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SqlSubmission',
            fields=[
                ('id', models.TextField(db_index=True, default=utils.shortcuts.rand_str, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(db_index=True)),
                ('username', models.TextField()),
                ('user_queries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', models.IntegerField(db_index=True, default=3)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('shared', models.BooleanField(default=False)),
                ('statistic_info', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('ip', models.TextField(null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.SqlProblem')),
            ],
            options={
                'db_table': 'sql_submission',
                'ordering': ('-create_time',),
            },
        ),
    ]
