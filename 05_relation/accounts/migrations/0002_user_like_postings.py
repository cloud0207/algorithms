# Generated by Django 3.2.18 on 2023-04-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_postings',
            field=models.ManyToManyField(related_name='like_users', to='blog.Posting'),
        ),
    ]
