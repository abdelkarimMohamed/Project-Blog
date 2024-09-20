# Generated by Django 5.1 on 2024-09-19 16:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_aboutpage_contactpage_postpage_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField()),
                ('bg_image', models.ImageField(upload_to='images/%y/%m/%d/background_images')),
                ('post_image', models.ImageField(upload_to='images/%y/%m/%d/post_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.DeleteModel(
            name='PostPage',
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['publish'], name='blog_post_publish_c4286e_idx'),
        ),
    ]
