# Generated by Django 4.2.7 on 2023-11-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_alter_submission_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='ai_result_analysis',
            field=models.TextField(blank=True, null=True),
        ),
    ]
