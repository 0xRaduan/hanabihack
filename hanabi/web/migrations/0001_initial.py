# Generated by Django 2.2.2 on 2019-06-29 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connected', jsonfield.fields.JSONField(blank=True)),
                ('result', jsonfield.fields.JSONField(blank=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='web.Language')),
                ('participants', models.ManyToManyField(related_name='sessions', to='web.Member')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='owners',
            field=models.ManyToManyField(related_name='language', to='web.Member'),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('answers', jsonfield.fields.JSONField()),
                ('creator', models.CharField(max_length=30)),
                ('result', models.IntegerField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='web.Session')),
            ],
        ),
    ]
