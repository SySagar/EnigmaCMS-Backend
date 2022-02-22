# Generated by Django 3.2.5 on 2022-02-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_domain_member_domain_expertise'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('visibility', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('ONLY-MEMBERS', 'Only-Members')], max_length=20)),
                ('time_stamp', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ManyToManyField(blank=True, related_name='Document_Creators', to='members.Member')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
