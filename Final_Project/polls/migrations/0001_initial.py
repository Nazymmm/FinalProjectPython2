# Generated by Django 4.0.1 on 2022-03-04 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCloud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]