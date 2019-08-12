# Generated by Django 2.1.11 on 2019-08-12 21:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Biography', 'Biography'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Romance', 'Romance'), ('Mystery', 'Mystery'), ('Sci Fi', 'Sci Fi'), ('Thriller', 'Thriller'), ('Superhero', 'Superhero')], default='Action', max_length=50)),
                ('year', models.CharField(max_length=4, null=True)),
                ('cast', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('runtime', models.CharField(max_length=20, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('file', models.FileField(default='', upload_to='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(default='What do you think of this movie', max_length=500, null=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date_comment', models.DateField(auto_now_add=True)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movies')),
            ],
        ),
        migrations.AddField(
            model_name='listmovies',
            name='movies',
            field=models.ManyToManyField(blank=True, to='movies.Movies'),
        ),
    ]