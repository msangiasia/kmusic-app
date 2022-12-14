# Generated by Django 3.2.6 on 2022-11-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_name', models.CharField(max_length=100)),
                ('art_username', models.CharField(max_length=100)),
                ('art_type', models.CharField(choices=[('R&B', 'RAPPER'), ('JZ', 'JAZZ'), ('HIPHOP', 'HIPPOP')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_type', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.EmailField(default='don', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
