# Generated by Django 4.1.2 on 2022-10-06 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('strength', models.IntegerField(default=0)),
                ('goat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expertises', to='main_app.goat')),
            ],
        ),
    ]
