# Generated by Django 4.0 on 2021-12-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('ansA', models.CharField(max_length=100)),
                ('ansB', models.CharField(max_length=100)),
                ('ansC', models.CharField(max_length=100)),
                ('ansD', models.CharField(max_length=100)),
                ('correct_ans', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
            ],
        ),
    ]