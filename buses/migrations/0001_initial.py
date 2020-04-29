# Generated by Django 3.0.5 on 2020-04-25 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('route_no', models.CharField(blank=True, default='', max_length=100)),
                ('bus_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stoppage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Next',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.Bus')),
                ('current', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current', to='buses.Stoppage')),
                ('next', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next', to='buses.Stoppage')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start', to='buses.Stoppage'),
        ),
        migrations.AddField(
            model_name='bus',
            name='stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop', to='buses.Stoppage'),
        ),
    ]
