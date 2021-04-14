# Generated by Django 2.2 on 2021-03-21 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0010_auto_20210318_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(blank=True, choices=[('paying', '待支付'), ('TRADE_FINISHED', '交易结束'), ('TRADE_SUCCESS', '成功'), ('TRADE_CLOSED', '超时关闭'), ('WAIT_BUYER_PAY', '交易创建')], default='paying', max_length=30, null=True, verbose_name='订单状态'),
        ),
    ]
