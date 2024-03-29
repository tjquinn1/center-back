# Generated by Django 2.0.4 on 2018-04-16 15:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20180416_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('non_billable', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='non_billable',
        ),
        migrations.AddField(
            model_name='time',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Task'),
        ),
    ]
