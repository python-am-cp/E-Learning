# Generated by Django 2.2 on 2019-04-10 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MapLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(default=None, max_length=50)),
                ('block_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('type', models.CharField(default=None, max_length=50)),
                ('description', models.TextField(default=None)),
                ('map_level_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.MapLevel')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default=None, max_length=50, unique=True)),
                ('password', models.CharField(default=None, max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('map_level_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.MapLevel')),
            ],
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=None)),
                ('video', models.URLField(default=None)),
                ('task_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.TextField(default=None)),
                ('task_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Task')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.User')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField(default=None)),
                ('output', models.TextField(default=None)),
                ('type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.TaskType')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Task')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='map_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.Map'),
        ),
    ]
