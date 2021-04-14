# Generated by Django 2.2 on 2021-03-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20210118_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(blank=True, choices=[('cancel', '待支付'), ('cancel', '取消'), ('success', '成功')], max_length=30, null=True, verbose_name='订单状态'),
        ),
    ]
