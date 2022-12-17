# Generated by Django 4.1.3 on 2022-11-26 22:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='the_default.jpg', upload_to='community_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(default='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('Community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumors.community')),
            ],
        ),
    ]