# Generated by Django 3.2.7 on 2022-01-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_pub', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
