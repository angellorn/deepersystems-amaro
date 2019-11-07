# Generated by Django 2.0.8 on 2019-11-07 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('like', models.IntegerField(verbose_name='Likes')),
            ],
            options={
                'db_table': 'like',
                'ordering': ['-like'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(upload_to='video/')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('theme', models.TextField(max_length=4000, verbose_name='Theme')),
            ],
            options={
                'db_table': 'video',
            },
        ),
        migrations.AddField(
            model_name='like',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video', verbose_name='Video'),
        ),
    ]