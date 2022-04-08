# Generated by Django 3.2.5 on 2022-04-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Created', 'Created'), ('Draft', 'Draft'), ('Rejected', 'Rejected')], default='Draft', max_length=20),
        ),
    ]