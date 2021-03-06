# Generated by Django 3.1.4 on 2020-12-26 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='marks',
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=150)),
                ('workplace', models.CharField(max_length=150)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssesmentMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('regarded_assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.assessment')),
            ],
        ),
    ]
