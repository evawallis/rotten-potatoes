# Generated by Django 4.2.10 on 2024-04-16 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('app', '0007_remove_useralbumrating_album_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlbumRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
        ),
    ]