# Generated by Django 2.0.4 on 2018-04-18 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(db_index=True, max_length=32, unique=True)),
                ('en_us', models.TextField(verbose_name='English')),
                ('zh_cn', models.TextField(verbose_name='简体中文')),
            ],
        ),
    ]