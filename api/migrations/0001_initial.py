# Generated by Django 3.2.9 on 2021-11-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predict_log',
            fields=[
                ('production_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('raw_image', models.TextField()),
                ('gray_image', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'predict_log',
            },
        ),
    ]