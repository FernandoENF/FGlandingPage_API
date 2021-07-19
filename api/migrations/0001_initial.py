# Generated by Django 3.2.5 on 2021-07-17 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=11)),
                ('code', models.CharField(blank=True, max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recommended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ref_by', to='api.student')),
            ],
        ),
    ]
