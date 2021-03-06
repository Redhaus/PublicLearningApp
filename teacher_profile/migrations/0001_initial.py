# Generated by Django 3.1 on 2020-08-16 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('school_profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text="Enter teacher's full name.", max_length=200, null=True)),
                ('teacher_bio', models.TextField(blank=True, help_text="Enter teacher's bio.", null=True)),
                ('subjects', models.TextField(blank=True, help_text='Enter the subjects you teach.', null=True)),
                ('grade_level', models.CharField(choices=[('K-5', 'K-5'), ('6-8', '6-8'), ('9-12', '9-12'), ('K-12', 'K-12'), ('K-8', 'K-8'), ('6-12', '6-12')], help_text='Enter the grade level the teacher instructs.', max_length=40, null=True)),
                ('profile_image', models.ForeignKey(blank=True, help_text='Upload profile picture.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('school_name', models.ForeignKey(blank=True, help_text='Select the school to which the teacher is connected.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_profile.schoolprofile')),
                ('user', models.OneToOneField(help_text='Select user who is the teacher connected to this profile.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher profile',
                'verbose_name_plural': 'Teacher profiles',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
