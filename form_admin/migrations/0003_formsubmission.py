# Generated by Django 4.2.4 on 2023-09-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_admin', '0002_remove_dynamicform_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('response_data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
