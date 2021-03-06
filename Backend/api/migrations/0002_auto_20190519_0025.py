# Generated by Django 2.1.4 on 2019-05-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(0, '매우 중요'), (1, '중요'), (2, '보통'), (3, '사소'), (4, '매우 사소')], verbose_name='중요도'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(0, '발의'), (1, '진행'), (2, '완료')], verbose_name='상태'),
        ),
        migrations.DeleteModel(
            name='TodoPriority',
        ),
        migrations.DeleteModel(
            name='TodoStatus',
        ),
    ]
