# Generated by Django 4.1.1 on 2022-10-01 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gym', models.CharField(choices=[('역삼', '역삼'), ('도곡', '도곡')], default='역삼', max_length=16, verbose_name='장소')),
                ('type', models.CharField(choices=[('웨이트', '웨이트'), ('부스터', '부스터'), ('펑셔널', '펑셔널'), ('몬스터', '몬스터')], default='웨이트', max_length=16, verbose_name='수업종류')),
                ('credit_count', models.PositiveIntegerField(verbose_name='크레딧 개수')),
                ('max_capacity', models.PositiveIntegerField(verbose_name='정원')),
                ('start_date', models.DateField(verbose_name='수업날짜')),
                ('start_time', models.TimeField(verbose_name='시작시간')),
                ('end_time', models.TimeField(verbose_name='종료시간')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='lesson.lesson', verbose_name='수업')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
