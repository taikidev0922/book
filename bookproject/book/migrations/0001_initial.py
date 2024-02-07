# Generated by Django 3.2 on 2024-02-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('business', 'ビジネス'), ('technology', 'テクノロジー'), ('philosophy', '哲学')], max_length=100)),
            ],
        ),
    ]