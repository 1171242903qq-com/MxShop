# Generated by Django 2.2 on 2021-01-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20210117_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(blank=True, choices=[('success', '成功'), ('cancel', '取消'), ('cancel', '待支付')], max_length=30, null=True, verbose_name='订单状态'),
        ),
    ]