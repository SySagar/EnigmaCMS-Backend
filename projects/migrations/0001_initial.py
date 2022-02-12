# Generated by Django 3.2.5 on 2022-02-12 02:57

from django.db import migrations, models
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('project_link', models.TextField(blank=True, null=True)),
                ('repository_link', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='default_project.jpg', upload_to='project_pics')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('tech_stack', django_mysql.models.ListCharField(models.CharField(max_length=40), max_length=1050, null=True, size=20)),
                ('members', models.ManyToManyField(to='members.Member')),
            ],
        ),
    ]
