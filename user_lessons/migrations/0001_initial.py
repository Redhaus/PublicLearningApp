# Generated by Django 3.1 on 2020-09-15 05:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('readings', '0001_initial'),
        ('lexis', '0001_initial'),
        ('teacher_profile', '0001_initial'),
        ('performances', '0001_initial'),
        ('continual_goals', '0001_initial'),
        ('key_questions', '0001_initial'),
        ('events', '0001_initial'),
        ('extensions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Enter the class title.', max_length=500)),
                ('class_description', models.TextField(blank=True, help_text='Enter the class description', null=True)),
                ('instructor', models.ForeignKey(help_text='Select user who is the teacher connected to this profile.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to='teacher_profile.teacherprofile')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(help_text='Enter the lesson title.', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('class_name', models.ForeignKey(help_text='Select class to this profile.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_name_lesson', to='user_lessons.classsubject')),
                ('event_collection', models.ForeignKey(blank=True, help_text='Enter the event for this lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='events.categoryeventcollection')),
                ('instructor', models.ForeignKey(blank=True, help_text='Select user who is the teacher who created the lesson.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile_lesson', to='teacher_profile.teacherprofile')),
                ('primary_reading', models.ForeignKey(blank=True, help_text='Enter the primary reading for this lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='readings.primaryfocus')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='LessonQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_questions', to='user_lessons.userlesson')),
                ('question_links', models.ForeignKey(help_text='Select questions for this lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_linked', to='key_questions.keyquestions')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonPerformances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_performances', to='user_lessons.userlesson')),
                ('performance_links', models.ForeignKey(help_text='Select any Performances for the lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performance_linked', to='performances.performances')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonLexis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('lexis_links', models.ForeignKey(help_text='Select any related lexis terms.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lexis_linked', to='lexis.lexis')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_lexis', to='lexis.lexis')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('goal_links', models.ForeignKey(help_text='Select goals related to the lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goal_linked', to='continual_goals.continualgoals')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_goals', to='user_lessons.userlesson')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonExtensions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('extension_links', models.ForeignKey(help_text='Select all related events.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extension_linked', to='extensions.extensions')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_extensions', to='user_lessons.userlesson')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonExplorations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('exploration_links', models.ForeignKey(help_text='Select all explorations for this lesson.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exploration_linked', to='readings.furtherexplorations')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_explorations', to='user_lessons.userlesson')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
