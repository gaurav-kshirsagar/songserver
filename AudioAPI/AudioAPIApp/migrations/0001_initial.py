# Generated by Django 3.2 on 2021-04-23 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('AudioBook', models.FileField(upload_to='Audiobook/')),
                ('Author', models.CharField(max_length=100)),
                ('Narrator', models.CharField(max_length=100)),
                ('Duration', models.PositiveIntegerField()),
                ('Upload_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Song', models.FileField(upload_to='Song/')),
                ('Duration', models.PositiveIntegerField()),
                ('Upload_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Podcast', models.FileField(upload_to='Podcast/')),
                ('Duration', models.PositiveIntegerField()),
                ('Upload_date', models.DateTimeField()),
                ('Host', models.CharField(max_length=100)),
                ('Participants', models.ManyToManyField(related_name='Participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
