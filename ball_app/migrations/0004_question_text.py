# Generated by Django 5.0.4 on 2024-05-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ball_app', '0003_remove_answer_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
