# Generated by Django 5.1.6 on 2025-03-13 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quizId', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionId', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=300)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
