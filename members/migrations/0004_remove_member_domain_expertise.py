# Generated by Django 3.2.5 on 2022-02-22 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_new_domain_expertise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='domain_expertise',
        ),
    ]