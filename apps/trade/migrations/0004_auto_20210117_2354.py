# Generated by Django 2.2 on 2021-01-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20201024_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(blank=True, choices=[('cancel', '待支付'), ('cancel', '取消'), ('success', '成功')], max_length=30, null=True, verbose_name='订单状态'),
        ),
    ]