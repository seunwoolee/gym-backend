# Generated by Django 4.1.1 on 2022-10-03 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_remove_reservation_canceled_reservation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='cancel_reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.reservation', verbose_name='취소 예약'),
        ),
    ]
