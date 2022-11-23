# Generated by Django 4.1.1 on 2022-10-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0008_purchasedcredit_credit_remaining_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='remaining_count',
            field=models.IntegerField(blank=True, help_text='사용 기간 만료 시 사용', null=True, verbose_name='남은 크레딧 개수'),
        ),
        migrations.DeleteModel(
            name='PurchasedCredit',
        ),
        migrations.CreateModel(
            name='PurchasedCredit',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('credit.credit',),
        ),
    ]