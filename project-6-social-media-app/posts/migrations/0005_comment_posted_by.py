# Generated by Django 4.2.16 on 2024-11-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='tom', max_length=200),
            preserve_default=False,
        ),
    ]
